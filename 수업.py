import requests as req
from bs4 import BeautifulSoup
from openpyxl import load_workbook
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = req.get( "https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20190908", headers = headers )

soup = BeautifulSoup( data.text, 'html.parser' )

