# import scrapy


# class HindinewsSpider(scrapy.Spider):
#     name = "HindiNews"
#     allowed_domains = ["www.aajtak.in"]
#     start_urls = ["https://www.aajtak.in"]

#     def parse(self, response):
#         # Extract text content from the webpage
#         text = response.xpath('//body//text()').getall()

#         # Tokenize Hindi text (You might need to use appropriate language detection libraries)
#         hindi_tokens = [token for token in text if any(ord(char) > 2300 for char in token)]


#         # Write tokens to a file line by line
#         with open('hindi_tokens.txt', 'a', encoding='utf-8') as f:
#             for token in hindi_tokens:
#                 f.write(token + '\n')
                
        
#         yield {
#             'hindi_tokens': hindi_tokens
#         }

######################################################################################################


# import scrapy


# class HindinewsSpider(scrapy.Spider):
#     name = "HindiNews"
#     allowed_domains = ["www.aajtak.in"]
#     start_urls = ["https://www.aajtak.in"]

#     def parse(self, response):
#         # Extract text content from the webpage
#         text = response.xpath('//body//text()').getall()

#         # Filter out English text and non-Hindi characters
#         hindi_text = []
#         hindi_characters = set(range(0x0900, 0x097F))  # Hindi Unicode range
#         for line in text:
#             for char in line:
#                 if ord(char) in hindi_characters:
#                     hindi_text.append(line)
#                     break

#         # Write Hindi text to a file
#         with open('hindi_text.txt', 'a', encoding='utf-8') as f:
#             for line in hindi_text:
#                 f.write(line + '\n')

#         # Yield the count of Hindi tokens
#         yield {
#             'hindi_token_count': len(hindi_text)
#         }
        
#         yield

######################################################################################################

# import scrapy
# from collections import Counter
# from scrapy.linkextractors import LinkExtractor

# class MySpider(scrapy.Spider):
#     name = 'HindiNews'
#     start_urls = ['https://www.aajtak.in']
#     allowed_domains = ['www.aajtak.in']
#     visited_urls = set()

#     def parse(self, response):
#         # Extract text content from the webpage
#         text = response.xpath('//body//text()').getall()        
        
#         # Join the text into a single string and split it into tokens using space as delimiter
#         text = ' '.join(text)
#         hindi_tokens = text.split()
        
        

#         # Tokenize Hindi text (You might need to use appropriate language detection libraries)
#         hindi_tokens = [token.strip() for token in text if any(ord(char) > 2300 for char in token)]

#         # Count token frequency
#         token_freq = Counter(hindi_tokens)

#         # Write token frequency for each token
#         with open('token_frequency.txt', 'a', encoding='utf-8') as f:
#             for token, freq in token_freq.items():
#                 f.write(f'{token}: {freq}\n')

#         # Extract other URLs
#         if response.url not in self.visited_urls:
#             self.visited_urls.add(response.url)
#             le = scrapy.linkextractors.LinkExtractor()
#             links = le.extract_links(response)
#             for link in links:
#                 if link.url not in self.visited_urls:
#                     yield scrapy.Request(link.url, callback=self.parse)


#         # Check if maximum iteration limit reached
#         if len(self.visited_urls) >= 2:
#             return

######################################################################################################


import scrapy


class HindinewsSpider(scrapy.Spider):
    name = "HindiNews"
    allowed_domains = ["www.aajtak.in"]
    start_urls = ["https://www.aajtak.in"]

    def parse(self, response):
        # Extract text content from the webpage
        text = response.xpath('//body//text()').getall()

        # Filter out English text and non-Hindi characters
        hindi_text = []
        hindi_characters = set(range(0x0900, 0x097F))  # Hindi Unicode range
        for line in text:
            for char in line:
                if ord(char) in hindi_characters:
                    hindi_text.append(line)
                    break

        # Write Hindi text to a file
        with open('hindi_text.txt', 'a', encoding='utf-8') as f:
            for line in hindi_text:
                f.write(line + '\n')

        # Yield the count of Hindi tokens
        yield {
            'hindi_token_count': len(hindi_text)
        }

        # Follow links on the page
        for next_link in response.xpath('//a/@href').getall():
            yield response.follow(next_link, callback=self.parse)
