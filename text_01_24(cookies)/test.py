#登录，获得cookie
#带着cookie去请求到书架的url->书架的内容
#必须得吧=把上面的两步操作连起来
#我们可以使用session进行请求->session你可以认为是一连串的请求。在这个过程中的cookie不会丢失。
import requests
#会话，交流
session=requests.session()
data={"loginName": "18392382730","password":"j1234@"}
#登录

url="https://passport.17k.com/ck/user/login"
session.post(url,data=data)
# print(resp.text)
# print(resp.cookies) #看cookies

#拿去书架上的书籍
resp=session.get('https://user.17k.com/ck/author2/shelf?page=1&appKey=2406394919')

print(resp.json())
