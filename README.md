# ZhihuCrawler
This is a www.zhihu.com crawler.

For example we have tags such as ```游戏```，```互联网```，I use the tags to classify all the datas.

## How it works

We all know that Zhihu needs your account number,password and verification code or sometimes tells you to choose the upside down Chinese characters. This version I should input verification code artificially and I haven't had a good solution if I occur the upside down Chinese characters.

### topic.py
First, I use selenium to have a automatic dirver to open zhihu, we need ```chromedriver``` or ```firefoxdirver```. Then open the "话题广场" to have all the top tags and its links stored. 

### topicContent.py
According to the topics I stored in topics.txt, open all the webs, use a css scroll to imitate a mouse scroll, and store all subtopics. Then in subtopics, click all "下一页" to the end to store all contents in tags' order.
