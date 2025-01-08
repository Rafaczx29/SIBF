import requests,re
from bs4 import BeautifulSoup as bsp
from menu import MAIN as mn

z=[]
x = bsp(requests.get('https://blog.cakap.com/nama-warna-dalam-bahasa-inggris/').text,'html.parser')
for a in x.find_all('span'):
    b=re.findall('<span style="font-weight: 400;">(.*?)</span>', str(a))
    if len(b)>0:
        p=b[0]
        z.append(p)
c=[]
for w in open('dumpig.txt', 'r').read().splitlines():
        print(w)
        c.append(w)
mn().CariNama(c, 'ig')