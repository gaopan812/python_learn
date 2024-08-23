import requests
import json

url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=3496eb9f-771b-4aa1-8fd7-1019bada3bb9'

# 您提供的 JSON 对象
data = {
    "msgtype": "news",
    "news": {
       "articles" : [
           {
               "title" : "中秋节礼品领取",
               "description" : "今年中秋节公司有豪礼相送",
               "url" : "www.qq.com",
               "picurl" : "http://res.mail.qq.com/node/ww/wwopenmng/images/independent/doc/test_pic_msg1.png"
           }
        ]
    }
}
response = requests.post(url, data=json.dumps(data))

# 输出响应的内容
print(response.text)

# 或者检查响应的状态码
print(response.status_code)