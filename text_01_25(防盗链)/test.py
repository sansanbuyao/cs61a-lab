#拿到conID
#拿到videoStatus返回的json.->srcURL
#修改srcURl里面的shuju
#下载视频
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                         ' AppleWebKit/537.36 (KHTML, like Gecko)'
                         ' Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
           #防盗链
           'Referer'   :'https://www.pearvideo.com/video_1791475'}

url="https://www.pearvideo.com/video_1791475"
conId=url.split("_")[1]

videoStatusUrl=f"https://www.pearvideo.com/videoStatus.jsp?contId={conId}&mrd=0.20209116746899114"
resp=requests.get(videoStatusUrl,headers=headers)
dic=resp.json() #会直接返回一个字典

srcUrl=dic['videoInfo']['videos']['srcUrl']
systemTime=dic['systemTime']

#替换,然后拿到视频链接
srcUrl=srcUrl.replace(systemTime,f"cont-{conId}")

#开始下载视频
with open("a.mp4",mode="wb") as f:
    f.write(requests.get(srcUrl).content)