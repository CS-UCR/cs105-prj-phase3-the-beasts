import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    
    def start_requests(self):
        urls = [
            'https://fortune.com/longform/fortune-500-trends-profits-losses/',
            'https://fortune.com/2015/06/16/fortune-500-fastest-growing-banks/',
        ]
        for url in urls:
             yield scrapy.Request(url=url, callback=self.parse)
                
    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
