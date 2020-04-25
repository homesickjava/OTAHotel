import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


driver = webdriver.Firefox()
driver.get(url='http://hotel.qunar.com/cn/hangzhou/?fromDate=2020-04-23&toDate=2020-04-24&cityName=%E6%9D%AD%E5%B7%9E')

time.sleep(10)

hotels = driver.find_element_by_id("hotel_lst_container")
hotelbodys= hotels.find_element_by_id("hotel_lst_body")
print(dir(hotelbodys)
items = hotelbodys.find_elements_by_class_name("item")
item = items.pop()
hotelprice = item.find_elements_by_xpath("//p[@class='price_new']/a[1]")
rmb = hotelprice[0].text    
hotelname = item.find_elements_by_xpath("//div[@class='operate fl_right']/a[1]")
name=hotelname[0].get_attribute("title")

with open('qinyi2020.txt','a+',newline='',encoding='utf-8') as f:
      f.write("\n")
      f.write("酒店名称++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
      f.write("\n")
      f.write(name)
      f.write("\n")
      f.write(rmb)
      f.write("\n")
      
alink = hotelname[0].get_attribute("href")
name.click()
time.sleep(10)
print(driver.current_url)
      
driver.get(url=alink)      
      
      
page = driver.page_source
html = BeautifulSoup(page, 'html.parser') # 从网页提取数据
content = html.find('section', class_= 'G_detailBG')
content1 = content.find('section', class_= 'G_section_1200 G_wrap')
content2 = content1.find('section', class_= 'G_section_1200 patch_MB20 G_blockBG G_blockBG_bott')
div1 = content2.find('div', class_= 'poi_tab')
div2 = div1.find('div', class_= 'boolToolWrapper')   
lists = div2.contents
      

with open('qinyi2020.txt','a+',newline='',encoding='utf-8') as f:
    f.write("        酒店房间列表-----------------------------------------------------------------------")
    for i in range(3,12):
        room=lists[i]
        #print(room.text)
        f.write(room.text)
    
content3 = content1.find('section', class_= 'G_section_1200 clearfix')
hoteldetail = content3.find('div', class_= 'hotel_desc').text
print(hoteldetail)      
      
dianping = content3.find('div', class_= 'cmt-list').text
print(dianping)      
      
with open('qinyi2020.txt','a+',newline='',encoding='utf-8') as f:
    f.write("        酒店详情-----------------------------------------------------------------------")
    f.write(hoteldetail)
    f.write("        评论信息-----------------------------------------------------------------------")
    f.write(dianping)
          
nextpagediv=content3.find('div', class_= 'cmt-pager')
nextpage=nextpagediv.find('div', class_= 'item next abled')
nextpage.click()