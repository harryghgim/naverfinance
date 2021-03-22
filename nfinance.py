import requests
from pandas.io.html import read_html
from bs4 import BeautifulSoup
from datetime import datetime
import ssl

# https://stackoverflow.com/questions/44629631/while-using-pandas-got-error-urlopen-error-ssl-certificate-verify-failed-cert
ssl._create_default_https_context = ssl._create_unverified_context 

# https://excelsior-cjh.tistory.com/109 pandas 부분은 이 블로그 도움을 많이 받았습니다.

df = read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13', header=0)[0]
df.종목코드 = df.종목코드.map('{:06}'.format)
df = df[['회사명','종목코드']]
df.rename(columns={"회사명": "name", "종목코드": "code"}, inplace=True)

company = input('종목명을 입력하세요: ')
try:
    myCode = df[df['name'] == company].code.values[0]
except IndexError:
    print('종목이름을 다시 확인해주세요')
    quit()
r = requests.get('https://finance.naver.com/item/main.nhn?code=' + myCode)
soup = BeautifulSoup(r.text, 'html.parser')
#print(soup.dl.text)
print(datetime.now().strftime('현재시각 %m월%d일, %I:%M %p'))
print(soup.find('div', class_='rate_info').dl.text)
print('👉', r.url)
