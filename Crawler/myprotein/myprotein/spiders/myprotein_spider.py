import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from myprotein.items import CrawlerItem
import json
import os
import time


class MyProteinSpider(CrawlSpider):
    name = "myprotein"

    allowed_domains = ['myprotein.es']
    start_urls = ['https://www.myprotein.es/nutrition.list//']

    rules = (
        Rule(LinkExtractor(allow=(r'.*\/*.list'), restrict_xpaths='//div[@class="sixItemCategories_container"]')),
        Rule(LinkExtractor(allow=(),
                           restrict_xpaths=(
                               '//div[@class="athenaProductBlock"]')
                           ), callback="parse_item", follow=True),
    )

    # Funcion que parsea el articulo concreto y lo guarda en un archivo JSON
    def parse_item(self, response):
        item = CrawlerItem()
        item["idProduct"] = response.xpath(
            "//div[@class='athenaProductReviews' and @id='athenaProductReviewsComponent']/@data-product-id").extract_first()
        item["nombreProducto"] = response.xpath("//h1[@class='productName_title']/text()").extract_first()
        item["precio"] = float(response.xpath(
            "//span[@class='productPrice_schema' and @data-schema='price']/text()").extract_first())
        item["descripcion"] = response.xpath(
            "//p[@class='productName_subtitle' and @data-product-name='subtitle']/text()").extract_first()
        item["numResenas"] = response.xpath(
            "//p[@class='athenaProductReviews_reviewCount Auto']/text()").extract_first()
        if item["numResenas"] is not None:
            item["numResenas"] = int(item["numResenas"].split()[0])
        item["stars"] = response.xpath(
            "//span[@class='athenaProductReviews_aggregateRatingValue']/text()").extract_first()
        if item["stars"] is not None:
            item["stars"] = float(item["stars"].split("\n")[1])
        item["tamanoRacion"] = response.xpath(
            "//div[@id='product-description-content-8']/div/p/text()").extract_first()
        if item["tamanoRacion"] is not None:
            item["tamanoRacion"] = item["tamanoRacion"][3:]
        item["racionesPorEnvase"] = response.xpath(
            "//div[@id='product-description-content-8']/div/p[2]/text()").extract_first()
        if item["racionesPorEnvase"] is not None:
            item["racionesPorEnvase"] = item["racionesPorEnvase"][3:]
        item["imageUrl"] =  response.xpath(
            "//div[@class='athenaProductImageCarousel_imageWrapper']/span/@data-path").extract_first()
        if item["imageUrl"] is not None:
            item["imageUrl"] = item["imageUrl"].split("/")[6]

        ## Informacion nutricional
        table_rows = (response.xpath(
            "//table[@class='nutritional-info-table'][1]/tbody/tr").getall())

        # Diccionario donde se almacenará la informacion nutricional
        infNutricional = []

        #Itera sobre la tabla de informacion nutricional
        for i in range(len(table_rows)):
            columns = response.xpath(
                f"//table[@class='nutritional-info-table'][1]/tbody/tr[{i}]/td").getall()

            # Iteracion sobre las columnas
            for j in range(len(columns)):
                # Cantidad del elemento
                element_quantity = response.xpath(
                    f"//table[@class='nutritional-info-table'][1]/thead/tr[1]/td[{j}]/strong/text()").extract_first()
                
                # Titulo del elemento
                skippable = response.xpath(
                    f"//table[@class='nutritional-info-table'][1]/tbody/tr[{i}]/td[@class='tal']/text()").extract_first()
                # Si el titulo no existe se pasa de almacenar el valor
                if(skippable is None):
                    element_title = response.xpath(
                        f"//table[@class='nutritional-info-table'][1]/tbody/tr[{i}]/td[1]/strong/text()").extract_first()

                    # Dato concreto
                    element_data = response.xpath(
                        f"//table[@class='nutritional-info-table'][1]/tbody/tr[{i}]/td[{j}]/text()").extract_first()
                    
                    # Solo se guardará el dato si existe en la tabla
                    if (element_data is not None):
                        info_element = {
                            "percentage": str(element_quantity),
                            "title": str(element_title),
                            "value": str(element_data) 
                        }
                        infNutricional.append(info_element)
                        
        item["infNutricional"] = infNutricional
        yield item

        # Guardamos los datos en un JSON para cada articulo
        # page = response.url.split("/")[-2]
        # filename = 'articles-%s.json' % page
        # with open(filename, 'w', encoding='utf8') as f:
        #     json.dump(item, f, ensure_ascii=False)
        # self.log('Saved file %s' % filename)

    
