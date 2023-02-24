import scrapy


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['http://peps.python.org/']

    def parse(self, response):
        numeric_table = response.css(
            'section[id="numerical-index"] tbody'
        )
        for pep in numeric_table.css('tr'):
            pep_link = pep.css('td a::attr(href)').get()
            yield response.follow(
                pep_link,
                callback=self.parse_pep_status
            )

    def parse_pep_status(self, response):
        title = response.css(
            'section[id="pep-content"] h1::text'
        ).get().split(' – ')
        data = {
            'number': title[0].split()[1],
            'name': title[1],
            'status': response.css('dd abbr::text').get(),
        }
        yield data
