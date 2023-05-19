#Remember to install the scrapy module

#Loads components from Scrapy 
from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader

#Creates class with the structure of the data that will be extracted
class Dato(Item):
    name=Field() 
    policeDepartment = Field()
    date = Field()
    cause = Field()
    id=Field()

#Creates the Spider
class ODMPSpider(Spider):
    name= "MiPrimerSpider" #Defines the Spider name
    start_urls = ['https://www.odmp.org/search/year/2021', #Creates a vector with the links where the data will be extracted
                  'https://www.odmp.org/search/year/2020',
                  'https://www.odmp.org/search/year/2019',
                  'https://www.odmp.org/search/year/2018',
                  'https://www.odmp.org/search/year/2017',
                  'https://www.odmp.org/search/year/2016',
                  'https://www.odmp.org/search/year/2015',
                  'https://www.odmp.org/search/year/2014',
                  'https://www.odmp.org/search/year/2013',
                  'https://www.odmp.org/search/year/2012',
                  'https://www.odmp.org/search/year/2011',
                  'https://www.odmp.org/search/year/2010',
                  'https://www.odmp.org/search/year/2009',
                  'https://www.odmp.org/search/year/2008',
                  'https://www.odmp.org/search/year/2007',
                  'https://www.odmp.org/search/year/2006',
                  'https://www.odmp.org/search/year/2005',
                  'https://www.odmp.org/search/year/2004',
                  'https://www.odmp.org/search/year/2003',
                  'https://www.odmp.org/search/year/2002',
                  'https://www.odmp.org/search/year/2001',
                  'https://www.odmp.org/search/year/2000',
                  'https://www.odmp.org/search/year/1999',
                  'https://www.odmp.org/search/year/1998',
                  'https://www.odmp.org/search/year/1997',
                  'https://www.odmp.org/search/year/1996'] 
    
    #Extracts Name, PoliceDepartment, Date and Cause given their xpaths
    def parse (self, response): 
        sel = Selector(response) 
        datos = sel.xpath('//section/article') 
        for i, elem in enumerate(datos):
            item= ItemLoader(Dato(), elem) 
            item.add_xpath('name','./div[2]/p[1]/a/text()')
            item.add_xpath('policeDepartment','./div[2]/p[2]/text()')
            item.add_xpath('date','./div[2]/p[3]/text()')
            item.add_xpath('cause','./div[2]/p[4]/text()')
            yield item.load_item()
            
#This code must be run in the Anaconda Prompt. 
# 1. Write cd in the prompt.
# 2. Introduce the path were the script is saved (e.g. C:\Users\user\Documents\Web scrapping) and press Enter
# 3. Type: scrapy runspider ODMP.py -o dataset.csv -t csv