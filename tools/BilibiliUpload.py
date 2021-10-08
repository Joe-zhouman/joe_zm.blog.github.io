import requests
import codecs, markdown
import re
 
 
def post_md(title, content, cookie):
     
    csrf = re.search(r"bili_jct=(.+?);", cookie).group(1)
    headers = {
               "Host": "api.bilibili.com",
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0",
               "Accept": "application/json, text/javascript, */*; q=0.01",
               "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en;q=0.3,en-US;q=0.2",
               "Accept-Encoding": "gzip, deflate, br",
               "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
               "Content-Length": "489",
               "Origin": "https://member.bilibili.com",
               "Connection": "keep-alive",
               "Referer": "https://member.bilibili.com/article-text/home?",
               "Cookie": cookie
               }
     
    data = {
            "title": title,
            "banner_url": "",   
            "content": content,
            "summary": '',
            "words": "",
            "category": "0",
            "list_id":"0",
            "tid": "4",
            "reprint": "0",
            "tags": "",
            "image_urls": "",   
            "origin_image_urls": "",    
            "dynamic_intro": "",    
            "media_id": "0",
            "spoiler": "0",
            "original": "0",
            "csrf": csrf
           }
     
    url = "https://api.bilibili.com/x/article/creative/draft/addupdate"
    r = requests.post(url, data, headers=headers)
    if r.status_code == 200:
        print("上传成功！请到草稿箱查看")