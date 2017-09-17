# coding=utf-8
import re

file= open('topics.txt', 'r')
s = file.readlines()
for k in s:
    name = k.split()[0] + '.txt'
    print(name)
    f = open(name, 'r', encoding='utf-8')
    second_contents = f.readlines()
    res = re.search(r'url = "(.*?)" name = "(.*?)"',second_contents[0])
    file_name = res.group(2)
    link_href = res.group(1)
    print (file_name, link_href)
    f.close()