import os
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

QUERY = str(input("SEARCH : "))

file = open('./Crawler_KISTI_'+QUERY+'.txt','w', encoding='utf-8')

Arr_URL = ['Default', 'Key', 'Target', 'Search', 'Count', 'Start', 'Sort', 'Type', 'Res', 'Query']

Arr_Value = ['http://openapi.ndsl.kr/itemsearch.do', '?keyValue=03323430', '&target=ARTI', '&searchField=BI', '&displayCount=100', '&startPosition=1', '&sortby=', '&returnType=xml', '&responseGroup=advance', '&query='+QUERY]

URL=''

for arr in range(len(Arr_URL)):
    URL += Arr_Value[arr]
print(URL)
headers = {
'Host': 'openapi.ndsl.kr',
'Connection': 'keep-alive',
'Upgrade-Insecure-Requests': 1,
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
'Cookie': '_ga=GA1.2.886947753.1522289626; WMONID=sRG64EHzxAF; JSESSIONID=aeEYqiOaIN5u1jVvsSp3Ru9n0imSEBf7AkwuFBwWXNlzDQrZM1lI2itgzZmg6Nfs.ar228_servlet_engine12'
}
req=urllib.request.Request(URL, headers=headers)
f = urllib.request.urlopen(req)
resultXML = f.read()
xmlsoup = BeautifulSoup(resultXML, 'html.parser')
items = xmlsoup.find_all('dissertation')
for item in items:
    print(item.dissertationtitle)
    file.write('-------------------------------\n')
    file.write(' 제목 : '+ item.dissertationtitle.get_text(strip=1)+'\n')
    file.write(' 내용 : '+ item.abstract.get_text(strip=1)+'\n')
    file.write(' 링크 : '+ item.deeplink.get_text(strip=1)+'\n')#본문의 링크를 가져오기 위해
    file.write('-------------------------------\n')
file.close()
'''
Default_URL = 'http://openapi.ndsl.kr/itemsearch.do'
Key_URL = '?keyValue=03323430'
Target_URL = '&target=ARTI'#ARTI=all/NART=학위제외/JAKO=국내/JAFO=해외/CFKO=국내회의/CFFO=해외회의/DIKO=국내학위
Search_URL = '&searchField=BI'#BI=all/TI=제목/SO=저널명/KW=키워드
Count_URL = '&displayCount=100'
Start_URL = '&startPosition=1'
Sort_URL = '&sortby='#default=정확도/title=논문명/jtitle=저널명/pubYear=발행일
Type_URL = '&returnType=xml'#xml/json
Res_URL = '&responseGroup=advance'#simple=URLx/advance=URL
Query_URL = '&query='+QUERY#검색질의어(UTF-8)
'''
