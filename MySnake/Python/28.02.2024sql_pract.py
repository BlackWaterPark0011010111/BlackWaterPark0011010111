import requests
from bs4 import BeautifulSoup

#rl = 'https://health-diet.ru/table_calorie/'
#
#eaders ={
#   'Accept': '*/*',
#   'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
#
#eq= requests.get(url, headers=headers)
#rc=req.text
#print(src)
#
with open("inde.html") as file:
   src= file.write()
   soup= BeautifulSoup(src, 'lxml')