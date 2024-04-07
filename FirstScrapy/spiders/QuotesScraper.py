import scrapy


class QuotesscraperSpider(scrapy.Spider):
    name = "QuotesScraper"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response):
        quotes = response.xpath("/html/body/div/div[2]/div[1]/div/span[1]/text()").extract()
        authors = response.xpath("/html/body/div/div[2]/div[1]/div/span[2]/small/text()").extract()
        
        for quote, author in zip(quotes, authors):
            quote_detail = {
                "quote": quote,
                "written by": author
            }
            
            yield quote_detail

