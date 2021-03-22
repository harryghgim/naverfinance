# naverfinance
[네이버 주식 웹사이트](https://finance.naver.com/)에서 당일 종목 정보(지수, 시세 등)를 가져오는 파이썬 프로그램입니다.

## 사용법
```
$ python nfinance.py
종목명을 입력하세요: 케이티
현재시각 03월22일, 08:15 PM

KT
오늘의시세 26,500 포인트
50 포인트 하락
0.19% 마이너스

👉 https://finance.naver.com/item/main.nhn?code=030200
```

## 라이브러리 설치
```
$ pip install requests pandas beautifulsoup4 # 또는
$ pip install -r requirements.txt
```

## 오류 메시지
- 종목명이 정확하지 않을 경우 `종목 이름을 다시 확인해주세요!` 메시지가 터미널에 나타납니다. 종목명은 한국거래소(KRX) 기준을 따릅니다.
- 오류메시지가 반복된다면 종목명이 영문인지 한글인지 다시 확인해주세요. 
- 예: `KT`(x) `케이티`(O) 

프로그램의 pandas 라이브러리 관련 내용은 [Excelsior-JH의 포스팅](https://excelsior-cjh.tistory.com/109)에서 영감을 얻었음을 밝힙니다.
