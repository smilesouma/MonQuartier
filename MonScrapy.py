import scrapy


class MonScrapy(scrapy.Spider):
    name = "MonScrapy"
    
    urls=[]
    for i in list(range(1,6)):
        urls.append('http://quotes.toscrape.com/page/{}/'.format(i))
    
    start_urls = urls[:]
        

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)


