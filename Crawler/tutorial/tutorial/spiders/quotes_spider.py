import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    start_urls = [
        'https://www.myprotein.es/nutrition/protein/whey-protein.list']
    

    rules = [
        Rule(LinkExtractor(allow=(),
                           restrict_xpaths=(
                               '//a[@class="athenaProductBlock_linkImage"]/@href')
        ) ,callback="parse_item" ),

    ]

    def parse(self, response):
        baseUrl = "https://www.myprotein.es/"

        urls = response.xpath(
            "//a[re:test(@class, 'athenaProductBlock_linkImage')]/@href").extract()
        
        for f in urls:
            new_url = baseUrl + f
            yield scrapy.Request(url=new_url, callback=self.parse_item)

        
    def parse_item(self, response):
        self.log("holis hago lo que hay que hacer")
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)


        
