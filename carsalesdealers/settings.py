# -*- coding: utf-8 -*-

# Scrapy settings for carsalesdealers project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'carsalesdealers'

SPIDER_MODULES = ['carsalesdealers.spiders']
NEWSPIDER_MODULE = 'carsalesdealers.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'carsalesdealers (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
#    'carsalesdealers.middlewares.CarsalesdealersSpiderMiddleware': 543,
     'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}
#from jaguar
#FEED_EXPORT_FIELDS = ['ANNONCE_LINK', 'FROM_SITE', 'SELLERTYPE', 'MINI_SITE_URL', 'MINI_SITE_ID', 'AGENCE_NOM', 'AGENCE_ADRESSE', 'AGENCE_CP', 'AGENCE_VILLE', 'AGENCE_DEPARTEMENT', 'EMAIL', 'WEBSITE', 'AGENCE_TEL', 'AGENCE_TEL_2', 'AGENCE_TEL_3', 'AGENCE_TEL_4', 'AGENCE_FAX', 'AGENCE_CONTACT', 'PAYS_DEALER', 'GARAGE_LICENCE', 'GARAGE_ID']
RETRY_TIMES = 10
RETRY_HTTP_CODES = [500, 503, 504, 416, 405, 400, 403, 404, 408]
DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
SPLASH_URL = 'http://localhost:8050/'
HTTP_PROXY = 'http://127.0.0.1:8128'
USER_AGENT_LIST = "/home/databiz41/useragents.txt"
# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
     'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
     'carsalesdealers.middlewares.RandomUserAgentMiddleware': 400,
     #'carsalesdealers.middlewares.RetryMiddleware': 200,	
     #'carsalesdealers.middlewares.ProxyMiddleware': 410,
     #'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
     #'scrapy.downloadermiddlewares.retry.RetryMiddleware': 200,
     #'carsalesdealers.middlewares.RetryChangeProxyMiddleware': 600,
    # 'scrapy_splash.SplashCookiesMiddleware': 723,
     #'scrapy_splash.SplashMiddleware': 725,
     #'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
#    'carsalesdealers.middlewares.MyCustomDownloaderMiddleware': 543,
}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}
FEED_EXPORT_FIELDS = ['ANNONCE_LINK', 'listing_page', 'DEALER_LINK', 'FROM_SITE', 'SELLERTYPE', 'MINI_SITE_URL', 'MINI_SITE_ID', 'AGENCE_NOM', 'AGENCE_ADRESSE', 'AGENCE_CP', 'AGENCE_VILLE', 'AGENCE_DEPARTEMENT', 'EMAIL', 'WEBSITE', 'AGENCE_TEL', 'AGENCE_TEL_2', 'AGENCE_TEL_3', 'AGENCE_TEL_4', 'AGENCE_FAX', 'AGENCE_CONTACT', 'PAYS_DEALER', 'GARAGE_LICENCE', 'GARAGE_ID', 'CAR_LINK']
# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'carsalesdealers.pipelines.CarsalesdealersPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 0
HTTPCACHE_DIR = 'httpcache'
HTTPCACHE_IGNORE_HTTP_CODES = []
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
#HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'
#HTTPCACHE_IGNORE_MISSING = False
