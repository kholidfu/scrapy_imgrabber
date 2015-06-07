# -*- coding: utf-8 -*-
from scrapy.contrib.pipeline.images import ImagesPipeline
import os
import scrapy
from urlparse import urlparse

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ImgrabberPipeline(object):
    def process_item(self, item, spider):
        #print "im in pipelines"
        return item


class CustomImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        for url in item["image_urls"]:
            yield scrapy.Request(url,
                headers={
                    "Referer": "%s://%s" % (urlparse(url).scheme, urlparse(url).netloc),
                    #"User-agent": "Googlebot",
                    "User-agent": "Mozilla/5.0",
                    })

    def file_path(self, request, response=None, info=None):
        # conditional 1 seperti flexicengli.com
        # fext = os.path.splitext(os.path.basename(request.url))[-1]
        # fname = "-".join(os.path.basename(request.url).split("-")[:-2])
        # return "full/%s" % fname + fext
        return "full/%s" % os.path.basename(request.url)


    def thumb_path(self, request, thumb_id, response=None, info=None):
        # conditional 1 seperti flexicengli.com
        # fext = os.path.splitext(os.path.basename(request.url))[-1]
        # fname = "-".join(os.path.basename(request.url).split("-")[:-2])
        # return "thumbs/%s/%s" % (thumb_id, fname + fext)
        return "thumbs/%s/%s" % (thumb_id, os.path.basename(request.url))
