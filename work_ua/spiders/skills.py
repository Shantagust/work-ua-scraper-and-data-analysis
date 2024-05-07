import scrapy
from scrapy.http import Response


class SkillsSpider(scrapy.Spider):
    name = "skills"
    allowed_domains = ["www.work.ua"]
    start_urls = ["https://www.work.ua/jobs-python/"]

    def parse(self, response: Response, **kwargs):
        for vacancy in response.css('div.card.card-hover.card-search.card-visited.wordwrap.job-link.js-job-link-blank'):
            detail_page = response.urljoin(vacancy.css('h2.cut-top.cut-bottom > a::attr(href)').get())
            yield response.follow(detail_page, self._parse_detail_page)

        next_page = response.css("ul.pagination > li")[-1].css("a::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

    @staticmethod
    def _parse_detail_page(response: Response) -> dict:
        skill_link = response.url
        salary = response.css('span.strong-500::text').get()
        vacancy_id = skill_link.split('/')[-2]
        for skill in response.css("span.label.label-skill.label-gray-100.mr-sm.mb-xs.mt-xs"):
            skill_name = skill.css('span.ellipsis::text').get()
            yield {
                "skill": skill_name,
                "salary": str(salary) if "грн" in salary else None,
                "vacancy_id": vacancy_id,
                "link": skill_link,
            }
