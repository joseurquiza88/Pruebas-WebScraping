# !pip install scrapy
import scrapy
class QuotesSpider(scrapy.Spider):
    name ="quotes"
    start_urls = ["https://quotes.toscrape.com/"]
    def parse(self, response):
        for q in response.css("span.text::text").getall():
            yeild {"quotes": q}
