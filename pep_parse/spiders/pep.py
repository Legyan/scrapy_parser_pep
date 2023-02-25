import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import ALLOWED_DOMAINS, START_URLS


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ALLOWED_DOMAINS
    start_urls = START_URLS

    def parse(self, response):
        numeric_table = response.css(
            'section[id="numerical-index"] tbody'
        )
        for pep in numeric_table.css('tr'):
            pep_link = pep.css('td a::attr(href)').get()
            yield response.follow(
                pep_link,
                callback=self.parse_pep
            )

    def parse_pep(self, response):
        title = response.css(
            'section[id="pep-content"] h1::text'
        ).get().split(' – ')
        data = {
            'number': title[0].split()[1],
            'name': title[1],
            'status': response.css('dd abbr::text').get(),
        }
        yield PepParseItem(data)
