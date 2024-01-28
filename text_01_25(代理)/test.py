#原理：通过第三方的一个机器去发起请求
import requests

#58.220.95.79:10000
proxies={"https":"https://58.220.95.79:10000"}

resp=requests.get("http://www.baidu.com",proxies=proxies)
resp.encoding='utf-8'
print(resp.text)