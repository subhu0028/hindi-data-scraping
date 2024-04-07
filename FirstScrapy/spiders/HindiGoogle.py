import scrapy


class HindigoogleSpider(scrapy.Spider):
    name = "HindiGoogle"
    allowed_domains = ["support-google-com.translate.goog"]
    start_urls = ["https://support-google-com.translate.goog/websearch/thread/197302979/my-google-searches-are-showing-up-in-hindi"]

    def parse(self, response):
        pass
