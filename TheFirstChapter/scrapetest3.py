from urllib.error import URLError, HTTPError
from urllib.request import urlopen

from bs4 import BeautifulSoup

"""

针对的问题：网站有可能不存在 或者 服务器宕机

    还有一种情况就是要访问的对象不存在

"""


def getTitle(url):
    # 这是关于页面读取的异常处理操作
    try:
        html = urlopen(url)
    except (HTTPError, URLError) as e:
        return None

    # 这里是关于页面分析可能产生的对象不存在的错误
    try:
        bf = BeautifulSoup(html.read())
        title = bf.body.h1
    except AttributeError as e:
        return None
    return title


# 方法调用
title = getTitle("http://pythonscraping.com/pages/page1.html")
if title is None:
    print("标题不存在")
else:
    print(title)
