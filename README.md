# naverfinance
네이버 주식 웹사이트에서 당일 종목 정보(지수, 시세 등)를 가져오는 파이썬 프로그램입니다.

## 사용법
`python naverFinance.py 종목명`

## 예시
```
$ python naverFinance.py SK하이닉스
현재시각 06월15일, 11:11 PM

SK하이닉스
오늘의시세 82,000 포인트
3,200 포인트 하락
3.76% 마이너스

👉 https://finance.naver.com/item/main.nhn?code=000660
```

## 필요 라이브러리
`pip install -r requirements.txt`를 터미널에 입력해 설치해주세요. `virtualenv` 또는 `venv`를 사용해 가상 환경에 라이브러리 설치를 권장합니다.

## 오류 메시지
- 종목명이 정확하지 않을 경우 `종목 이름을 다시 확인해주세요!` 메시지가 터미널에 나타납니다. 종목명은 한국거래소(KRX) 기준을 따릅니다.
- 오류메시지가 반복된다면 종목명이 영문인지 한글인지 다시 확인해주세요. 
- 예: `KT`(x) `케이티`(O) 

프로그램의 pandas 라이브러리 관련 내용은 [Excelsior-JH의 포스팅](https://excelsior-cjh.tistory.com/109)에서 영감을 얻었음을 밝힙니다.
