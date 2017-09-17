# coding = utf-8

from selenium import webdriver
import time
from bs4 import BeautifulSoup
import pymysql

#SQL
#conn = pymysql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock', user='root', passwd=None, db='mysql')
#cur = conn.cursor()
#cur.execute("SELECT Host,User FROM user")

driver=webdriver.Chrome("C:/chromedriver/chromedriver.exe")                  #用chrome浏览器打开
driver.get("http://www.zhihu.com")                                           #打开知乎我们要登录
time.sleep(2)                                                                #让操作稍微停一下
driver.find_element_by_link_text('登录').click()                              #找到‘登录’按钮并点击
time.sleep(1)
                          
driver.find_element_by_name('account').send_keys('897380742@qq.com') 
time.sleep(1)

driver.find_element_by_name('password').send_keys('djh123456')
time.sleep(1)

yanzhengma=input('验证码:')
driver.find_element_by_name('captcha').send_keys(yanzhengma)
#找到登录按钮，并点击
driver.find_element_by_css_selector('div.button-wrapper.command > button').click()
cookie=driver.get_cookies()
driver.find_element_by_css_selector('div.button-wrapper.command > button').click()
cookie=driver.get_cookies()
time.sleep(1)


def Crawler(link, filename):
    filename = filename + '.txt'
    driver.get(link)
    time.sleep(2)

    def scroll(driver):  
        driver.execute_script("""   
            (function () {   
                var y = document.body.scrollTop;   
                var step = 100;   
                window.scroll(0, y);   
      
      
                function f() {   
                    if (y < document.body.scrollHeight) {   
                        y += step;   
                        window.scroll(0, y);   
                        setTimeout(f, 50);   
                    }  
                    else {   
                        window.scroll(0, y);   
                        document.title += "scroll-done";   
                    }   
                }   
      
      
                setTimeout(f, 1000);   
            })();   
            """) 
        time.sleep(15)
    
    scroll(driver)    
#    def execute_times(times):
#        for i in range(times + 1):
#            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#            time.sleep(2)
#    execute_times(10)

# this function can be used in pulling content of answers

#    def Next():
#        while(1):
#            a = driver.find_element_by_link_text('更多')
#            if(a == 0):
#                break
#            else:
#                a.click()
#            time.sleep(2)
#    Next()
                
    
    html=driver.page_source
    soup1=BeautifulSoup(html,'lxml')
    games = soup1.select('div.blk a[target="_blank"]')
    file = open(filename, 'w',encoding='utf-8-sig')
    #topics = soup1.select('li.zm-topic-cat-item')

    for game in games:
        #topic_href = 'https://www.zhihu.com/topics' + '#' + topic.text
        href = 'http://www.zhihu.com'+game.get('href')
        file.write('url = "' + href + '" ')
        file.write('name = "'+game.text.strip()+'"\n')
        
    file.close()
    print('end' + filename)
    
def main():
    file= open('topics.txt', 'r')
    s = file.readlines()
    for k in s:
        Crawler(k.split()[1], k.split()[0])
        
if __name__ == '__main__':
    main()
    print('end all')

#cur.close()
#conn.close()