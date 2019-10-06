import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    start_urls = [
        'https://www.prozis.com/es/es/alimentacion-saludable/barritas-y-snacks-para-llevar/muffins']
    

    rules = [
        Rule(LinkExtractor(allow=(),
            restrict_xpaths=('//a[@class="w-100 h-100 m-0 p-0"]/@href')
        ) ,callback="parse_item" ),

    ]

    def parse(self, response):
        baseUrl = "https://www.prozis.com/es/es/prozis/"

        urls = response.xpath(
            "//a[re:test(@class, 'w-100 h-100 m-0 p-0')]/@href").extract()
        
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


        
