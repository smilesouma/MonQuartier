# -*- coding: utf-8 -*-
"""
test scrapy: web crawling pour CBDATA7

developed by Eddie Rajaonarivelo ( e.rajaonar(at)ymail.com )

"""

import scrapy
import csv
from MonScrapy.items import delitItem


class violence(scrapy.Spider):
    name = "violence"
    allowed_domains = ["www.linternaute.com"]
    
    # lecteur du fichier csv (liste code postaux-ville) et récuperation des colonnes
    with open('code_postaux.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        # ignorer la première ligne (nom des colonnes)
        next(csvfile)
        mydict = {rows[0]:rows[1] for rows in readCSV}

    
    urls=[]
    for i, j in mydict.items():
        urls.append('http://www.linternaute.com/actualite/delinquance/{}/ville-{}/violence'.format(j,i))
    
    start_urls = urls[:]
        

    def parse(self, response):

        rubrique = 'violence'

        path_tableau1 = '//div[4]/table/tbody//tr'
        path_tableau2 = '//div[8]/table/tbody//tr'
        path_tableau3 = '//div[11]/table/tbody//tr'
        path_tableau4 = '//div[13]/table/tbody//tr'
        
        tableau1 = response.xpath(path_tableau1)
        tableau2 = response.xpath(path_tableau2)
        tableau3 = response.xpath(path_tableau3)
        tableau4 = response.xpath(path_tableau4)
        
        for elt in tableau1:
            item = delitItem()
            item['ville'] = response.xpath('//h1/span[@itemprop="name"]/text()').extract()
            item['titre'] = " ".join(response.xpath('//h2/span/text()')[0].extract().split()[:2])
            item['rubrique'] = rubrique
            item['delit'] = elt.xpath('td[1]//text()').extract_first()
            item['donnees'] = elt.xpath('td[2]//text()').extract_first()
            item['equivalence'] = elt.xpath('td[3]//text()').extract_first()
            yield item
        
        for i in tableau2:
            item = delitItem()
            item['ville'] = response.xpath('//h1/span[@itemprop="name"]/text()').extract()
            item['titre'] = " ".join(response.xpath('//h2/span/text()')[0].extract().split()[:2])
            item['rubrique'] = rubrique
            item['delit'] = i.xpath('td[1]//text()').extract_first()
            item['donnees'] = i.xpath('td[2]//text()').extract_first()
            item['equivalence'] = i.xpath('td[3]//text()').extract_first()
            yield item

        for i in tableau3:
            item = delitItem()
            item['ville'] = response.xpath('//h1/span[@itemprop="name"]/text()').extract()
            item['titre'] = " ".join(response.xpath('//h2/span/text()')[0].extract().split()[:2])
            item['rubrique'] = rubrique
            item['delit'] = i.xpath('td[1]//text()').extract_first()
            item['donnees'] = i.xpath('td[2]//text()').extract_first()
            item['equivalence'] = i.xpath('td[3]//text()').extract_first()
            yield item
        
        for i in tableau4:
            item = delitItem()
            item['ville'] = response.xpath('//h1/span[@itemprop="name"]/text()').extract()
            item['titre'] = " ".join(response.xpath('//h2/span/text()')[0].extract().split()[:2])
            item['rubrique'] = rubrique
            item['delit'] = i.xpath('td[1]//text()').extract_first()
            item['donnees'] = i.xpath('td[2]//text()').extract_first()
            item['equivalence'] = i.xpath('td[3]//text()').extract_first()
            yield item