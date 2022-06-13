from pprint import pprint
from turtle import title
from unicodedata import category
from bili.items import BiliItem
import scrapy
import json

class BilispiderSpider(scrapy.Spider):
    name = 'bilispider'
    allowed_domains = ['https://api.bilibili.com/']
    weeknum = 167

    def start_requests(self):
        start_urls = ['https://api.bilibili.com/x/web-interface/popular/series/one?number=167']
        for i in range(50):
            url = 'https://api.bilibili.com/x/web-interface/popular/series/one?number=%d' % (self.weeknum-i)
            start_urls.append(url)
        for url in start_urls:
            yield scrapy.Request(url=url, callback = self.parse)

    def parse(self, response):
        items = []

        #获取json数据
        data = json.loads(response.text)
        list = data['data']['list']


        for i in list:
            item = BiliItem()

            aweek = self.weeknum
            title = i['title']
            name = i['owner']['name']
            mid = i['owner']['mid']
            bvid = i['bvid']
            category = i['tname']
            play_link = i['short_link']
                        
            stat = i['stat']
            view = stat['view']
            coin = stat['coin']
            reply = stat['reply']
            like = stat['like']
            favorite = stat['favorite']
            
            item['title'] = title
            item['name'] = name
            item['mid'] = mid
            item['bvid'] = bvid
            item['category'] = category
            item['play_link'] = play_link
            
            item['view'] = view
            item['coin'] = coin
            item['reply'] = reply
            item['like'] = like
            item['favorite'] = favorite
            item['aweek'] = aweek

            items.append(item)
        self.weeknum-=1

        return items

