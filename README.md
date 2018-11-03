# scrapy..
Scrapy 爬虫项目

windows项目流程：
1 切换至目标文件夹，Shift+鼠标右键在此处打开命令窗口
2 scrapy startproject xxx
3 cd xxx
4 scrapy genspider xxSpider www.xxx.com
5 Pycharm或者其他编辑器打开进行coding
...
6 scrapy crawl xxSpider运行爬虫


Scrapy文件结构:
  __init__  初始化文件
  items.py  定义要抓取的字段
  pipelines.py  进行信息后序处理，当spider抓取到内容（item）后就将其送至这里,然后对其清洗、去重，保存到文件或者数据库
  middlewares.py  中间件，主要是对功能的拓展你可以添加一些自定义 比如添加随机user -agent添加 proxy 
  settings.py 设置文件，用来设置爬虫的默认信息，相关功能开启与否
  spiders/  在这个文件夹下，编写自己定义的spider，可以在此文件夹下定义多个爬虫文件
  
items存储到mysql数据库：
  1 使用MySQL Front软件创建一个数据库，例如127.0.0.1  dangdang  goods   [title,link,comments]
  2 开启MySQL服务，右键计算机点击管理，服务，找到MySQL相关服务开启
  3 settings.py文件打开pipelines.py的注释，如下，然后在pipelines.py里面处理数据，将其存入数据库中
    ITEM_PIPELINES = {
        'dangdang.pipelines.DangdangPipeline': 300,
    }

  
