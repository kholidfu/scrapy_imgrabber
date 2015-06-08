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
        # this is the downloader
        for url in item["image_urls"]:
            yield scrapy.Request(url,
                headers={
                    "Referer": "%s://%s" % (urlparse(url).scheme, urlparse(url).netloc),
                    #"User-agent": "Googlebot",
                    "User-agent": "Mozilla/5.0",
                    })

    def file_path(self, request, response=None, info=None):
        """
        override method from parent class.
        """
        # conditional 1 seperti flexicengli.com
        # fext = os.path.splitext(os.path.basename(request.url))[-1]
        # fname = "-".join(os.path.basename(request.url).split("-")[:-2])
        # return "full/%s" % fname + fext

        # tukang pecah belah disini
        # if kitchen in basename: path full/kitchen-design/basename

        fname = os.path.basename(request.url).lower()
        home_element_keywords = ["lamp", ]
        kitchen_keywords = ["kitchen", ]
        living_room_keywords = ["living", ]

        if any(i in fname for i in kitchen_keywords):
            return "full/%s/%s" % ("kitchen-design", fname)
        if any(i in fname for i in living_room_keywords):
            return "full/%s/%s" % ("living-room", fname)
        if any(i in fname for i in home_element_keywords):
            return "full/%s/%s" % ("home-element", fname)
        return "full/%s/%s" % ("unsorted", fname)


    def thumb_path(self, request, thumb_id, response=None, info=None):
        # conditional 1 seperti flexicengli.com
        # fext = os.path.splitext(os.path.basename(request.url))[-1]
        # fname = "-".join(os.path.basename(request.url).split("-")[:-2])
        # return "thumbs/%s/%s" % (thumb_id, fname + fext)
        return "thumbs/%s/%s" % (thumb_id, os.path.basename(request.url))
