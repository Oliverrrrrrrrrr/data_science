# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BiliPipeline:
    fp = None

    def open_spider(self,spider):
        print('开始爬虫')
        self.fp = open('bili.txt','w',encoding='utf-8')

    def process_item(self, item, spider):
        try:
            line = str(dict(item)) + "\n"
            self.fp.write(line)
        except:
            pass
        return item

    def close_spider(self,spider):
        print('结束爬虫')
        self.file.close()
    