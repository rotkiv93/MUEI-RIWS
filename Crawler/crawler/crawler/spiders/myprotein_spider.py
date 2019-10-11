import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import json
import os
import time


class MyProteinSpider(scrapy.Spider):
    name = "myprotein"

    start_urls = [
        'https://www.myprotein.es/nutrition/protein/whey-protein.list']

    rules = [
        Rule(LinkExtractor(allow=(),
                           restrict_xpaths=(
                               '//a[@class="athenaProductBlock_linkImage"]/@href')
                           ), callback="parse_item"),

    ]

    # Funcion que itera sobre la URL basica e itera sobre los articulos
    def parse(self, response):
        baseUrl = "https://www.myprotein.es/"

        urls = response.xpath(
            "//a[re:test(@class, 'athenaProductBlock_linkImage')]/@href").extract()

        for f in urls:
            new_url = baseUrl + f
            yield scrapy.Request(url=new_url, callback=self.parse_item)

    # Funcion que parsea el articulo concreto y lo guarda en un archivo JSON
    def parse_item(self, response):
        item = {}
        item["nombreProducto"] = response.xpath("//h1[@class='productName_title']/text()").extract_first()
        item["precio"] = response.xpath(
            "//span[@class='productPrice_schema' and @data-schema='price']/text()").extract_first()
        item["descripcion"] = response.xpath(
            "//p[@class='productName_subtitle' and @data-product-name='subtitle']/text()").extract_first()
        item["numResenas"] = response.xpath(
            "//p[@class='athenaProductReviews_reviewCount Auto']/text()").extract_first()
        item["stars"] = response.xpath(
            "//span[@class='athenaProductReviews_aggregateRatingValue']/text()").extract_first()
        item["tamanoRacion"] = response.xpath(
            "//div[@id='product-description-content-8']/div/p/text()").extract_first()
        item["racionesPorEnvase"] = response.xpath(
            "//div[@id='product-description-content-8']/div/p[2]/text()").extract_first()

        ## Informacion nutricional
        table_rows = (response.xpath(
            "//table[@class='nutritional-info-table'][1]/tbody/tr").getall())

        # Diccionario donde se almacenará la informacion nutricional
        infNutricional = {}

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
                        # self.log("cabecera: %s - %s - %s" % (element_title, element_quantity, element_data))
                        header = str(element_title) + " " + str(element_quantity)
                        infNutricional[header] = str(element_data)
            
        item["infNutricional"] = infNutricional

        # Guardamos los datos en un JSON para cada articulo
        page = response.url.split("/")[-2]
        filename = 'articles-%s.json' % page
        with open(filename, 'w', encoding='utf8') as f:
            json.dump(item, f, ensure_ascii=False)
        self.log('Saved file %s' % filename)

    
