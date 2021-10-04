#Exemple Riccard
import scrapy
from llibrescraper.items import LlibrescraperItem
from scrapy.loader import ItemLoader

class LlibreSpider2(scrapy.Spider):
    name = 'llibres_l'
    start_urls = ['https://onallibres.cat/botiga']

    def parse(self, response):              
        for products in response.css('div.book-result'):
            l = ItemLoader(item=LlibrescraperItem(), selector=products)
            l.add_css('Title', '#prodCont > h3 > a')
            l.add_css('Author','p.book-result-subtitle')
                
            l.add_css('Price','p.book-result-price')
                
            l.add_css('link','#prodCont > h3 > a::attr("href")')
                
            
            yield l.load_item()

        next_page = response.css('body > div.content > div.d-flex.flex-row.mx-auto > div.cat-main-cont.w-100 > div.mt-2.mb-5.catalog-container-main > div.row.mt-5.mb-5 > div > nav > ul > li:nth-child(12) > a').attrib['href']
        
        while next_page is not None: 
            yield response.follow(next_page, callback = self.parse)

