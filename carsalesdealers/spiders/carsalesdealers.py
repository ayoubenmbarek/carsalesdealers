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
        name = "carsalesdealers06-11"
        handle_httpstatus_list = [200, 302, 301]#, 500]#, 403]
        allowed_domains = ['carsales.com.au']
	    #sudo docker run -p 5023:5023 -p 8050:8050 -p 8051:8051 scrapinghub/splash
        #start_urls = ['https://www.carsales.com.au/dealer-services/dealers?s=4500&sb=featured'] 
        start_urls = ['https://www.carsales.com.au/dealer-services/dealers?sb=featured'] #new
        #start_urls = ['https://www.carsales.com.au/dealer-services/dealers?q=(And.Market.Car._.Status.1._.Department.Parts+%26+Accessories.)&sb=dealername'] #per department
	#start_urls = ['https://www.carsales.com.au/dealer-services/dealers?sb=featured']
                     
        download_delay = 0
        download_timeout = 280
        
	#change separator awk 'gsub(",",";")' latest5_carsales_2017_09_v4.csv
        def parse(self, response):
            headers = {
                ':authority':'carsales.mobi',
                ':method':'GET',
                ':path':'/mobiapi/v2/membership/membername',
                ':scheme':'https',
                'accept':'*/*',
                'accept-encoding':'gzip, deflate, sdch, br',
                'accept-language':'fr-FR,fr;q=0.8,en-US;q=0.6,en;q=0.4',
                'authorization':'Basic d2luYXBwOndpbmFwcDEyMw==',
                'content-type':'application/json',
                'cookie':'__csnMobiExp__smartsearch_5_new=Default; _ga=GA1.2.2049612815.1507049770; _gid=GA1.2.949223249.1507049770; gaclientId=2049612815.1507049770; __CSNDWUSL=Fwcl0MNDvz9GU5pBjGqi58a6pnYXJBHt4z7sVHZR3voKxiHoIZqcxSmEcWmNnF8PMeHLhPoiJ4Y6YZA6wJW6NXApF0XhVDd2bkm8So0Q9z7F1+jzhpJNsraAKCfo7CurEEritGw6XJRxFI98xtHutmidKhwXgqvKUQv45m1kynUzmW6DoHBNVulkhORfyqzq5uT6lliMuxHrHNd63VTiLZEnrIFm8nFbdyqfLITTm72pxyqTaz9J/XLvFpTIMbaO9rZg6UfE0UdHuA3ojES5Ea7GL/NM6Vgq; ak_bmsc=222885B10D0DB42CAB328AE45C2C24600210A25F3D43000021C3D459EB8BD11C~pl303oHPmXUPdLeZzUQS/M6+FeSHcB7c4lcFWoEDp/XdBeIAzd7pZoMSI9iui/AoPGfZ+GYmRmvFn5HB6dxTr/69KMyxV98qDNDCYWRdavKkWopXlIJkBRePMWNwKwpVV7rZANklijFbU35RETb2KFErE846+9osJwGuF+drfnjTT88IxG3bAas/9DKOMgMSnu5RZX1GdFx8RJ+YgrXaHnD2XiEZ7Mlc0dpQfpjNH5EJz4gzZqL5IDEh0Nvoh4hV2+; bm_mi=4A45CC4C66B700DF35C0FDEC1F22D441~TNkEC0JmiRGg2T9aTn16XsAIXlYlfAJVe4ms6DuxhsYA/9krhgi3FVrYUBdcyT4XgLRiQK9/k0IhCTicqgmiEafKZcS0t2ZLvQZhqun5gclObnIU8OOcvTdpzYOgnHhdTgJo8pIGOnrIuApBXCqGWKPCjxUX499cT0pr/BGRUtJorVKfuLV7IvmwAuhFoEpyCwGYF7jE1PCx7HxNe4ZhX/v4LzJO/seRt4x6Q8TFkqz6XY0CCZxvaSrnLDvbdYD+VX+nMvv+JDx5kBB27eH53A==',
                'referer':'https://carsales.mobi/',
                'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Mobile Safari/537.36'
        }
            #container =  response.css('div.listing-item')          
            #container = response.xpath('//div[@class="listing"]/div[@class="listing-item"]')
            container = response.css('div.listing-item')
            #myItem = CarsalesdealersItem()
            for list_dealers in container:
                myItem = CarsalesdealersItem()
                href = list_dealers.xpath(".//a[contains(text(), 'More')]/@href").extract_first()
                #href = list_dealers.xpath(".//a[contains(text(), 'More')]/@href").extract_first()
                cc2 = href.split('/')
                myItem["AGENCE_ID"]  = cc2[-1]
                myItem["listing_page"] = response.url
                #myItem["NAME"] = list_dealers.xpath('.//h4[@class="tenant-color"]/strong/text()').extract_first()
                myItem["NAME"] = list_dealers.css('h4.tenant-color >strong ::text').extract_first()
                #myItem["PHONE"] = list_dealers.xpath('.//span[@class="phone"]/@data-number').extract_first()
                myItem["PHONE"] = list_dealers.css('span.phone ::attr(data-number)').extract_first()
                #myItem["ADRESSE"] = list_dealers.xpath('.//div[@class="col-xs-8"]/p[1]/text()').extract_first()
                myItem["ADRESSE"] = list_dealers.css('div.col-xs-8 > p ::text').extract_first()
                #myItem['code'] = list_dealers.xpath('.//div[@class="col-xs-8"]/p[2]/text()').extract_first()
                myItem['code'] = list_dealers.css('div.col-xs-8 > p::text').extract()[1]
                #departmaent = list_dealers.xpath("//div/ul/li[contains(text(), 'Service Department')]/following-sibling::li/text()").extract()[1]
                
                full_url = response.urljoin(href)
                myItem["DEALER_LINK"] = full_url
                request = scrapy.Request(full_url, callback=self.second_page)
                request.meta['myItem'] = myItem
                yield request
            for i in range(1,501):#find number of pages(496 all) 525 from2,46 ## 0409 501pg
                next = 'https://www.carsales.com.au/dealer-services/dealers?s='+str(i*15)+'&sb=featured'
                yield scrapy.Request(next, callback=self.parse)
            #next_page_href = response.xpath('//a[@class="page"]/@href').extract()[-1]
           # next_page_href = response.css('a.page::attr(href)').extract()[-1]
            #if next_page_href:
              #  next_page = response.urljoin(next_page_href)
               # yield scrapy.Request(next_page, callback=self.parse)
        
        def second_page(self, response):
                myItem = response.meta["myItem"] 
                myItem["WEBSITE"] = response.xpath('//div[@class="layout-section text-right"]/a/@href').extract_first()
                #myItem["DEALER_LINK"] = response.url
                yield myItem
                
             
                
        
