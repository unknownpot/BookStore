import scrapy

class booksSpider(scrapy.Spider):
    name = "books_spider"

    def start_requests(self):
        urls = [
            "http://books.toscrape.com/catalogue/page-1.html"
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response): 
        
        for b in response.css("article.product_pod"):
            link = b.css("div.image_container a img::attr(src)").get()
            title = b.css("h3 a::attr(title)").get()
            price = b.css("div.product_price p.price_color::text").get()

            yield {
        	'image_url' : link,
            'book_title' : title,
            'product_price': price
        	}
        
        next_page = response.css('ul.pager li.next a::attr(href)').get()
        if next_page is not None:
            
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page,callback = self.parse)
       
       
        #with open(filename, 'wb') as f:
         #   f.write(response.body)

        #self.log("Saved file as %s" %filename)