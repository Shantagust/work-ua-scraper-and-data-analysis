BOT_NAME = "work_ua"
SPIDER_MODULES = ["work_ua.spiders"]
NEWSPIDER_MODULE = "work_ua.spiders"
ROBOTSTXT_OBEY = False
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
