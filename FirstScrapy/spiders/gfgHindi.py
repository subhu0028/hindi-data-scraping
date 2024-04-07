import scrapy


class GfghindiSpider(scrapy.Spider):
    name = "gfgHindi"
    allowed_domains = ["www-geeksforgeeks-org.translate.goog"]
    start_urls = ["https://www-geeksforgeeks-org.translate.goog/geeksforgeeks-python-foundation-course-learn-python-in-hindi/"]

    def parse(self, response):
        pass
