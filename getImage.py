import requests
import re
content=requests.get('http://www.quanyouyg.com/mobile').text
match_src=re.compile('(src=(http://.*?\.jpg))"',re.S)

lists=re.findall(match_src,content)
print(lists)
# n=1
# for item in lists:
#     html = requests.get(item)
#     print(html)
#     n=int(n)+1
#     with open('imgs/picture'+str(n)+'.jpg', 'wb') as file:
#       file.write(html.content)