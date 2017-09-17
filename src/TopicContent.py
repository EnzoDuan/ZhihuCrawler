# coding=utf-8

from selenium import webdriver
import time
from bs4 import BeautifulSoup
import pymysql
import re
import os
import shutil

driver=webdriver.Chrome("C:/chromedriver/chromedriver.exe")                  #用chrome浏览器打开
driver.get("http://www.zhihu.com")                                           #打开知乎我们要登录
time.sleep(2)                                                                #让操作稍微停一下
driver.find_element_by_link_text('登录').click()                              #找到‘登录’按钮并点击
time.sleep(0.5)
                          
driver.find_element_by_name('account').send_keys('897380742@qq.com') 
time.sleep(0.5)

driver.find_element_by_name('password').send_keys('djh123456')
time.sleep(0.5)

yanzhengma=input('验证码:')
driver.find_element_by_name('captcha').send_keys(yanzhengma)
#找到登录按钮，并点击
driver.find_element_by_css_selector('div.button-wrapper.command > button').click()
cookie=driver.get_cookies()
driver.find_element_by_css_selector('div.button-wrapper.command > button').click()
cookie=driver.get_cookies()
time.sleep(2)


def Crawler(link, filename, dir_name):
    filename = dir_name + '/' + filename + '.txt'
    driver.get(link)
    time.sleep(1)

    driver.find_element_by_link_text('精华').click()
    time.sleep(0.5)
    html_=driver.page_source
    soup=BeautifulSoup(html_,'lxml')
    intro = soup.select('div.zm-editable-content')
    file = open(filename, 'w',encoding='utf-8')
    file.write('introduce = "' + intro[0].text[:-2] + '"\n')
        
    while(1):
        html2=driver.page_source
        time.sleep(1)
        soup1=BeautifulSoup(html2,'lxml')
        pages = soup1.select('span.zg-gray-normal')
        count = 0
        for p in pages:
            count = count + 1

        authors=soup1.select('span.author-link-line a.author-link')
        authors_alls=[]
        authors_hrefs=[]
        for author in authors:
            authors_alls.append(author.get_text())
            authors_hrefs.append('http://www.zhihu.com'+author.get('href'))
        authors_intros_urls=soup1.select('span.bio')
        authors_intros=[]
        for authors_intros_url in authors_intros_urls:
            authors_intros.append(authors_intros_url.get_text())

        contents = soup1.select('div[class="zh-summary summary clearfix"]')
        hrefs = soup1.select('div[class="expandable entry-body"] link')
        titles = soup1.select('a.question_link')
        for content,authors_all,authors_href,authors_intro, href_t, title in zip(contents, authors_alls,authors_hrefs,authors_intros, hrefs, titles):
            href = 'http://www.zhihu.com'+href_t.get('href')
# First links
            file.write('href = "'+href+'" ')
# Second Questions           
            file.write('title = "' + title.text.strip() + '" ')
# Third authors 
            data={
                'author':authors_all,
                'href':authors_href,
                'intro':authors_intro
            }
            file.write('author = "' + str(data) + '" ')
# Forth contents
            file.write('content = "' + content.text[:-5].strip() + '" \n')
# End one page
        if(((count == 2) & (pages[0].text != "上一页")) | (count == 0)):
            print('end ' + filename)
            file.close()
            return
        driver.find_element_by_link_text('下一页').click()

    
def main():
    file= open('topics.txt', 'r')
    s = file.readlines()
    for k in s:
        name = k.split()[0] + '.txt'
        if(os.path.exists(k.split()[0]) == True):
            shutil.rmtree(k.split()[0])
        time.sleep(0.1)
        os.mkdir(k.split()[0])
        f = open(name, 'r', encoding = 'utf-8')
        second_contents = f.readlines()
        for a in second_contents:
            res = re.search(r'url = "(.*?)" name = "(.*?)"',a)
            file_name = res.group(2)
            link_href = res.group(1)
            Crawler(link_href, file_name, k.split()[0])
        f.close()
    file.close()
        
if __name__ == '__main__':
    main()
    print('end all')