#coding=utf-8 

from bs4 import BeautifulSoup
import requests
import re #引入正则表达

r = requests.get('https://2.python-requests.org//zh_CN/latest/user/quickstart.html')
soup = BeautifulSoup(r.text,'lxml')
for link in soup.find_all(href=re.compile("http")):
	if re.match(r'.*python-requests.*',link.get('href')):
		print(link.get('href'))
	
	
print("done")
# 指纹识别

# 全栈url采集，并且输出项目文档


# 设置Cookie

# 设置代理