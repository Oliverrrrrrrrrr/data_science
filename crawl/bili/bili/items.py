# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BiliItem(scrapy.Item):
    # define the fields for your item here like:
    #静态变量
    title = scrapy.Field()
    name = scrapy.Field()
    mid = scrapy.Field()
    bvid = scrapy.Field()
    category = scrapy.Field()
    play_link = scrapy.Field()
    aweek  = scrapy.Field()
    view = scrapy.Field()
    coin = scrapy.Field()
    reply = scrapy.Field()
    like = scrapy.Field()
    favorite = scrapy.Field()
