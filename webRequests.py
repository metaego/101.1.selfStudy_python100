# 01. 웹서버에 요청하고 응답받기

# 학습내용
# : 웹 서버에 접속하여 웹 페이지 정보를 요청하고 서버로부터 응답 객체를 받는 과정 이해

import requests
# requests:웹 서버에 요청하고 응답 받는 과정을 처리하는 파이썬 라이브러리

# 특정 사이트 url을 변수 url에 할당
url = "https://www.python.org/"

# request의 get()함수를 사용하여 웹 서버에 get요청을 보내고
# 특정 url을 저장한 변수(url)을 함수의 매개변수로 전달
# 웹 서버가 응답한 내용을 변수 resp에 저장
resp = requests.get(url)

# resp 변수가 저장하고 있는 웹 서버의 응답 결과를 print()함수로 출력
print(resp)

url2 = "https://www.python.org/1"
resp = requests.get(url2)
print(url2)