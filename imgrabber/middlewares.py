from scrapy.contrib.spidermiddleware.referer import RefererMiddleware


class SetHeaders(RefererMiddleware):
    def process_requests(self, request, spider):
        request.headers.setdefault("Referer", "http://fazook.com")
