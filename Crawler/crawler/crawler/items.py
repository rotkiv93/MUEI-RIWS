# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    nombreProducto = scrapy.Field()
    precio = scrapy.Field()
    descripcion = scrapy.Field()
    numResenas = scrapy.Field()
    stars = scrapy.Field()
    ## Macros
    tamanoRacion = scrapy.Field()
    racionesPorEnvase = scrapy.Field()
    energiaPorRacion = scrapy.Field()
    energia100G = scrapy.Field()
    energiaIR = scrapy.Field()
    grasasPorRacion = scrapy.Field()
    grasas100G = scrapy.Field()
    grasasIR = scrapy.Field()
    hidratosPorRacion = scrapy.Field()
    hidratos100G = scrapy.Field()
    hidratosIR = scrapy.Field()
    proteinasPorRacion = scrapy.Field()
    proteinas100G = scrapy.Field()
    proteinasIR = scrapy.Field()
    salPorRacion = scrapy.Field()
    sal100G = scrapy.Field()
    salIR = scrapy.Field()




