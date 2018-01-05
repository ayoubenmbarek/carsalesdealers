#!/usr/bin/env python
# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy import Request
from ..items import CarsalesdealersItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
import ast
from scrapy.conf import settings
from scrapy_splash import SplashRequest
from datetime import datetime  
from datetime import timedelta 
from selenium import webdriver
from selenium.webdriver.common.by import By

class CarsalesDealersSpider(scrapy.Spider):
        name = "lastspider2-05-01-18" #carsalesdealersperdepartment0410 contain cache of the most listing page
        #handle_httpstatus_list = [302, 301]#, 500]#, 403] #commented 04-01-18
        allowed_domains = ['carsales.com.au']
	    #sudo docker run -p 5023:5023 -p 8050:8050 -p 8051:8051 scrapinghub/splash
        start_urls = ['https://www.carsales.com.au/dealer-services/dealers?sb=featured'] 
        #start_urls = ['https://www.carsales.com.au/dealer-services/dealers?s=1800&q=(And.Market.Car._.Status.1._.Department.Service+Department.)&sb=dealername'] #per department
        #start_urls = ['https://www.carsales.com.au/dealer-services/dealers?q=(And.Market.Car._.Status.1._.Department.Showroom.)&sb=dealername']#showroom
	#start_urls = ['https://www.carsales.com.au/dealer-services/dealers?s=15&q=(And.Market.Car._.Status.1._.Department.Showroom.)&sb=dealername']#the last
	#start_urls = ['https://www.carsales.com.au/dealer-services/dealers?q=(And.Market.Car._.Status.1._.Department.Showroom.)&sb=dealername']
                     
        download_delay = 0
        download_timeout = 180
        
        
	#change separator awk 'gsub(",",";")' latest5_carsales_2017_09_v4.csv
        def parse(self, response):
                headers = {
                ':authority':'carsales.mobi',
                ':method':'GET',
                #':path':'/mobiapi/v2/membership/membername',
                ':scheme':'https',
                'accept':'*/*',
                'accept-encoding':'gzip, deflate, sdch, br',
                'accept-language':'fr-FR,fr;q=0.8,en-US;q=0.6,en;q=0.4',
                'authorization':'Basic d2luYXBwOndpbmFwcDEyMw==',
                'content-type':'application/json',
               # 'cookie':'__csnMobiExp__smartsearch_5_new=Default; _ga=GA1.2.2049612815.1507049770; _gid=GA1.2.949223249.1507049770; gaclientId=2049612815.1507049770; __CSNDWUSL=Fwcl0MNDvz9GU5pBjGqi58a6pnYXJBHt4z7sVHZR3voKxiHoIZqcxSmEcWmNnF8PMeHLhPoiJ4Y6YZA6wJW6NXApF0XhVDd2bkm8So0Q9z7F1+jzhpJNsraAKCfo7CurEEritGw6XJRxFI98xtHutmidKhwXgqvKUQv45m1kynUzmW6DoHBNVulkhORfyqzq5uT6lliMuxHrHNd63VTiLZEnrIFm8nFbdyqfLITTm72pxyqTaz9J/XLvFpTIMbaO9rZg6UfE0UdHuA3ojES5Ea7GL/NM6Vgq; ak_bmsc=222885B10D0DB42CAB328AE45C2C24600210A25F3D43000021C3D459EB8BD11C~pl303oHPmXUPdLeZzUQS/M6+FeSHcB7c4lcFWoEDp/XdBeIAzd7pZoMSI9iui/AoPGfZ+GYmRmvFn5HB6dxTr/69KMyxV98qDNDCYWRdavKkWopXlIJkBRePMWNwKwpVV7rZANklijFbU35RETb2KFErE846+9osJwGuF+drfnjTT88IxG3bAas/9DKOMgMSnu5RZX1GdFx8RJ+YgrXaHnD2XiEZ7Mlc0dpQfpjNH5EJz4gzZqL5IDEh0Nvoh4hV2+; bm_mi=4A45CC4C66B700DF35C0FDEC1F22D441~TNkEC0JmiRGg2T9aTn16XsAIXlYlfAJVe4ms6DuxhsYA/9krhgi3FVrYUBdcyT4XgLRiQK9/k0IhCTicqgmiEafKZcS0t2ZLvQZhqun5gclObnIU8OOcvTdpzYOgnHhdTgJo8pIGOnrIuApBXCqGWKPCjxUX499cT0pr/BGRUtJorVKfuLV7IvmwAuhFoEpyCwGYF7jE1PCx7HxNe4ZhX/v4LzJO/seRt4x6Q8TFkqz6XY0CCZxvaSrnLDvbdYD+VX+nMvv+JDx5kBB27eH53A==',
                'referer':'https://carsales.mobi/',
                'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Mobile Safari/537.36'
                 }
                #container =  response.css('div.listing-item')          
                container = response.xpath('//div[@class="listing"]/div[@class="listing-item"]')
                #myItem = CarsalesdealersItem()
                for list_dealers in container:
                        myItem = CarsalesdealersItem()
                        href = list_dealers.xpath(".//a[contains(text(), 'More')]/@href").extract_first()
                        cc2 = href.split('/')
                        myItem["MINI_SITE_ID"]  = cc2[-1]
                        myItem["listing_page"] = response.url
                        myItem["AGENCE_NOM"] = list_dealers.xpath('.//h4[@class="tenant-color"]/strong/text()').extract_first()
                        myItem["AGENCE_TEL"] = list_dealers.xpath('.//span[@class="phone"]/@data-number').extract_first()

			#commented 08-11
                        agence_details = list_dealers.xpath('.//div[@class="col-xs-8"]/p[1]/text()').extract_first()
			cc = agence_details.split(',')
			#myItem["AGENCE_ADRESSE"] = list_dealers.xpath('.//div[@class="col-xs-8"]/p[1]/text()').extract()
			myItem["AGENCE_ADRESSE"] = cc[0]
			
			myItem['AGENCE_VILLE'] = cc[-1]
			
			myItem['AGENCE_CP'] = list_dealers.xpath('.//div[@class="col-xs-8"]/p[2]/text()').extract_first()
			department = myItem['AGENCE_CP'].split(' ')
			myItem["AGENCE_DEPARTEMENT"] = department[0]
			#myItem['AGENCE_VILLE'] = cc[-1].strip()
                        #myItem['code'] = list_dealers.xpath('.//div[@class="col-xs-8"]/p[2]/text()').extract_first()
                        #myItem["AGENCE_DEPARTEMENT"] = list_dealers.xpath('.//div[@class="services"]/ul//li/text()').extract()
                       # try:
                       #         myItem["AGENCE_DEPARTEMENT"] = list_dealers.xpath('//div[@class="col-xs-8"]/p[1]/text()').extract()[2]
                       # except:
                               # pass
                       #try:
                         #       myItem['AGENCE_CP'] = list_dealers.xpath('//div[@class="col-xs-8"]/p[1]/text()').extract()[1]
                        #except:
                              #  pass
                        
                        full_url = response.urljoin(href) 
                        myItem["DEALER_LINK"] = full_url
                        request = scrapy.Request(full_url, headers=headers, callback=self.second_page)
                        request.meta['myItem'] = myItem
                        yield request
                        
                #link_container = response.css('div.pagination.top')
                #for link in link_container:
                       # next = link.css('a ::attr(href)').extract()[-1]
                       # if next:
                               # next_page = response.urljoin(next)
                               # yield scrapy.Request(next_page, headers=headers, callback=self.parse)
                for i in range(1,513):#504 all pages so 505 is the last 06-11
                        next = 'https://www.carsales.com.au/dealer-services/dealers?s='+str(i*15)+'&sb=featured'
                        #next = 'https://www.carsales.com.au/dealer-services/dealers?s='+str(i*15)+'&q=(And.Market.Car._.Status.1._.Department.Service+Department.)&sb=dealername'
                        #next = 'https://www.carsales.com.au/dealer-services/dealers?s='+str(i*15)+'&q=(And.Market.Car._.Status.1._.Department.Showroom.)&sb=dealername'
                        yield scrapy.Request(next, callback=self.parse)
            #next_page_href = response.xpath('//a[@class="page"]/@href').extract()[-1]
           # next_page_href = response.css('a.page::attr(href)').extract()[-1]
            #if next_page_href:
              #  next_page = response.urljoin(next_page_href)
               # yield scrapy.Request(next_page, callback=self.parse)
        
        def second_page(self, response):
                myItem = response.meta["myItem"]
                #try: 
                #myItem["WEBSITE"] = response.xpath('//div[@class="layout-section text-right"]/a/@href').extract_first()
                myItem["WEBSITE"] = response.xpath('//a[@class="btn"]/@href').extract()
                #except:
                       #pass
                #myItem["DEALER_LINK"] = response.url
                #agence_details = response.xpath('//div[@class="col-xs-6"]/div/p[1]/strong/text()').extract()
                #myItem["AGENCE_ADRESSE"] = response.xpath('//div[@class="col-xs-6"]/div/p[1]/strong/text()').extract_first()
                #cc = agence_adresse.split(',')
               # myItem["AGENCE_ADRESSE"] = cc[0]
               # myItem['AGENCE_VILLE'] = cc[-1]
                #myItem['AGENCE_DEPARTEMENT'] = response.xpath('//div[@id="tab-service"]/div/div/div/p/strong/text()').extract()
                #myItem['AGENCE_DEPARTEMENT'] = response.xpath('//option[contains(text(), "Service Department")]/@value').extract()
                #myItem["AGENCE_DEPARTEMENT"] = response.xpath('//div[@class="col-xs-6"]/div/p[1]/strong/text()').extract()[3]
                
                myItem['ANNONCE_LINK'] = response.url
                myItem['FROM_SITE'] = 'carsales'
                
                myItem['SELLERTYPE'] = ''
                myItem['MINI_SITE_URL'] = response.url
                garage_id = myItem['MINI_SITE_URL'].split('-') #the number on mini_site_id
                myItem['GARAGE_ID'] = garage_id[-1]
                
                
                ad_link = response.xpath('//div[@class="tab-stock-list" and not(@id="tab-used-cars")]/a[1]/@href').extract_first(default='')
                adresse_ville_cp = ' '.join(response.xpath('//div[@id="tab-showroom"]//strong[br]/text()').extract()).strip(' \n\r\t').encode('utf-8')
                #myItem['AGENCE_CP'] = adresse_ville_cp.split('\r\n')[1].strip(' \r\n\t') if len(adresse_ville_cp.split('\r\n')) > 1 else ''
                #myItem['AGENCE_VILLE'] = adresse_ville_cp.split(',')[1].replace(myItem['AGENCE_CP'], '').strip(' \r\n\t').encode('utf-8') if len(adresse_ville_cp.split(',')) > 1 else ''
                
                myItem['CAR_LINK'] = ad_link
                
                #if ad_link != '':
                 #       req = scrapy.Request(ad_link, callback=self.plus_data)
                     #   req.meta['myItem'] = myItem
                       # yield req
               # else:
                        #yield myItem

                yield myItem
                
       # def plus_data(self, response):
           #    myItem = response.meta['myItem']
            #    myItem['GARAGE_LICENCE'] = ''
             #   garage_licence = response.xpath('//*[@class="ad-panel"][1]/div/@data-media-motive-url').extract_first(default='')
              #  if garage_licence != '' :
               #         garage_licence = re.findall('lmct=([^/]*)', garage_licence)
                #        myItem['GARAGE_LICENCE'] = garage_licence[0] if len(garage_licence) > 0 else ''
                #myItem['GARAGE_ID'] = ''
                #garage_id = response.xpath('//script[contains(text(), "dealer_id")]/text()').extract_first(default='')
                #if garage_id != '':
                     #   garage_id = re.findall('dealer_id=([^&]*)', garage_id)
                     #   myItem['GARAGE_ID'] = garage_id[0] if len(garage_id) > 0 else ''

                #yield myItem
                
             
                
        
