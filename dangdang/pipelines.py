# -*- coding: utf-8 -*-
import pymysql    #        写入数据库中去,pipelines.py需要先去settings.py打开注释,做后序处理
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DangdangPipeline(object):
    def process_item(self, item, spider):
        conn = pymysql.connect(host="127.0.0.1",user ="root", passwd ="root", db = "dangdang", port=3306) #MySQL
        cur =conn.cursor()
        for i in range(0, len(item["title"])):
            title = item["title"][i]
            link = item["link"][i]
            comment = item["comment"][i]

            sql = "insert into goods(title,link,comment) values('"+title+"','"+link+"','"+comment+"')"

            cur.execute(sql)
            conn.commit()

        conn.close()
        return item
