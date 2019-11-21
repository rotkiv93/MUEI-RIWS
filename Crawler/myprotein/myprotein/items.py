# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class CrawlerItem(scrapy.Item):
    idProduct = scrapy.Field() 
    nombreProducto = scrapy.Field()
    itemURL = scrapy.Field()
    precio = scrapy.Field()
    descripcion = scrapy.Field()
    numResenas = scrapy.Field()
    stars = scrapy.Field()
    tamanoRacion = scrapy.Field()
    racionesPorEnvase = scrapy.Field()
    infNutricional = scrapy.Field()
    imageUrl = scrapy.Field()
    categoria = scrapy.Field()





