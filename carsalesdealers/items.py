# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CarsalesdealersItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    listing_page = scrapy.Field()
    AGENCE_NOM = scrapy.Field()
    AGENCE_TEL = scrapy.Field()
    AGENCE_ADRESSE = scrapy.Field()
    code = scrapy.Field()
    AGENCE_ID = scrapy.Field()
    WEBSITE =  scrapy.Field()
    DEALER_LINK = scrapy.Field()
    AGENCE_DEPARTEMENT = scrapy.Field()
    GARAGE_LICENCE = scrapy.Field()
    GARAGE_ID = scrapy.Field()
    AGENCE_VILLE = scrapy.Field()
    AGENCE_CP = scrapy.Field()
    CAR_LINK = scrapy.Field()
    EMAIL = scrapy.Field()
    AGENCE_TEL_2 = scrapy.Field()
    AGENCE_TEL_3 = scrapy.Field()
    AGENCE_TEL_4 = scrapy.Field()
    AGENCE_FAX = scrapy.Field()
    AGENCE_CONTACT = scrapy.Field()
    PAYS_DEALER = scrapy.Field()
    
    ANNONCE_LINK = scrapy.Field()
    FROM_SITE = scrapy.Field()
    SELLERTYPE = scrapy.Field()
    MINI_SITE_URL = scrapy.Field()
    MINI_SITE_ID = scrapy.Field()

   # pass
