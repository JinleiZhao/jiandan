from lxml import etree
import requests
from selenium import webdriver
from time import sleep
from urllib import request

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
    "Referer":"http://jandan.net/",
}
url = 'http://jandan.net/pic'
content = requests.get(url,headers=headers).text
# print(content)
# html = etree.HTML(content)
# img_list = html.xpath('//div[@class="acv_comment"]/p/img')[0]
# print(img_list.attrib)

driver = webdriver.Firefox()
driver.get(url)
# sleep(4)
img_list =driver.find_elements_by_tag_name('img') #查询当前页面所有图片
for img in img_list:
    src = img.get_attribute('src').replace('thumb180','large')#thumb180是显示的静态图片
    name = src.rsplit('/',1)[1]
    print(src )
    path = "E:\\Note\\Python\\9.18pachong\\jiandan\\img\\" + name
    request.urlretrieve(src,path)
    # res = requests.get(src,headers=headers)
    # with open(path,'wb') as f:
    #     f.write(res.content)
    print('%s is down'%name)
    sleep(1)
driver.quit()
# img_list = html.xpath('//img')
# for img in img_list:
#print(img.attrib.get('src'))

