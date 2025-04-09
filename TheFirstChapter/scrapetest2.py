from urllib.request import urlopen

from bs4 import BeautifulSoup

"""

针对的问题是前面读取的网页内容没有得到有效地处理，阅读困难

"""

html = urlopen("http://pythonscraping.com/pages/page1.html")

# BeautifulSoup 实际上是一个超级好用的文本处理方式，尤其擅长处理网页文件
bf = BeautifulSoup(html.read())
print(bf)
