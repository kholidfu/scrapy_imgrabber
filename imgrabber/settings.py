# -*- coding: utf-8 -*-
from imgrabber.spiders.wp_spiders import WPSpider
from urlparse import urlparse
import os

target_dir = WPSpider.target
target_dir = urlparse(target_dir).netloc
# Scrapy settings for imgrabber project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'Googlebot'

SPIDER_MODULES = ['imgrabber.spiders']
NEWSPIDER_MODULE = 'imgrabber.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'imgrabber (+http://www.yourdomain.com)'

SPIDER_MIDDLEWARES = {
    'scrapy.contrib.spidermiddleware.referer.RefererMiddleware': True,
    # 'imgrabber.middlewares.SetHeaders': 400,
}

ITEM_PIPELINES = {"imgrabber.pipelines.CustomImagesPipeline": 2}
# ITEM_PIPELINES = {"scrapy.contrib.pipeline.images.ImagesPipeline": 1}  # ori

IMAGES_STORE = os.path.join("/home/banteng/Desktop/imgcontainer", target_dir)
# IMAGES_THUMBS = {"small": (50, 50), "big": (270, 270),}

# filter out small images
IMAGES_MIN_HEIGHT = 351
IMAGES_MIN_WIDTH = 351

DOWNLOAD_DELAY = 5
