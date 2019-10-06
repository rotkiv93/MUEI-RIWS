import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://www.prozis.com/es/es/alimentacion-saludable/barritas-y-snacks-para-llevar/barritas//es/es/alimentacion-saludable/barritas-y-snacks-para-llevar/muffins']
    

    rules = [
        Rule(LinkExtractor(allow=(), restrict_xpaths=(
            "//a[@class='w-100 h-100 m-0 p-0']")), follow=True),
        Rule(LinkExtractor(
            allow=("//a[@class='w-100 h-100 m-0 p-0']")), callback="parse_item")
    ]

    def parse_item (self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

    def parse(self, response):
        item_url = response.xpath(
            "//a[@class='w-100 h-100 m-0 p-0']/@href").extract_first()
        self.logger.error(item_url)
        


        
