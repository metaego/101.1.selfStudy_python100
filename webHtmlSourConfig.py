# 02. 웹 페이지 소스코드 확인하기

# 학습내용
# :웹 서버가 보내주는 응답 객체의 여러 속성 중에서 HTML 소스코드를 구분할 수 있음

# request의 get함수는 웹 서버에 get 요청을 보내고 웹 서버가 보내주는 응답 객체를 받는다.
# HTML의 소스 코드 경우 응답 객체의 test 속성에 저장되어 있다.



import requests

url = "https://www.python.org/"
resp = requests.get(url)

html = resp.text

print(html)
