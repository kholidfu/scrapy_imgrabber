from imgrabber.items import ImgrabberItem
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor
import scrapy
from urlparse import urljoin, urlparse
import re


class WPSpider(CrawlSpider):
    name = "wpspider"
    target = "http://example.com"
    allowed_domains = [urlparse(target).netloc]
    start_urls = [urljoin(target, "wp-content/uploads/")]
    # start_urls = [urljoin(target, "i/2015/06/")]
    rules = [
        Rule(
        LxmlLinkExtractor(), #restrict_xpaths=("(//a)[position()>1] ")),
        callback='parse_item',
        follow=True,)
    ]


    def parse_item(self, response):
        hxs = Selector(response)
        item = ImgrabberItem()
        img_relative_urls = hxs.xpath("//a/@href").extract()
        img_container = []
        for url in img_relative_urls:
            img_absolute_url = urljoin(response.url, url)
            # some filterisasi
            # 1. remove thumbnail version
            # if img_absolute_url.split("-")[-1].split(".")[0].split("x")[0].isalpha():
            if "x" not in img_absolute_url.split("-")[-1].split(".")[0]:
                # image appended
                img_container.append(img_absolute_url)

        item["image_urls"] = img_container
        yield item
