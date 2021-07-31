# 04. BeautifulSoup 객체 만들기

# 학습내용
# beautifulsoup 라이브러리를 이용하여 정적 웹 페이지에서 정보를 추출


# 웹 서버로부터 HTML 소스코드를 가져온 다음 HTML 태그 구조를 해석하기 위한 과정이 필요
# 해당 과정을 파싱이라 함
# 파싱(parsing): HTML 소스 코드를 해석하는 것

import requests 
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Seoul_Metropolitan_Subway"
resp = requests.get(url)
html_src = resp.text

soup =BeautifulSoup(html_src, 'html.parser')
print(type(soup))
print("\n")

print(soup.head)
print("\n")

print(soup.body)
print("\n")


print("title 태그 요소: ", soup.title)
print("title 태그 이름: ", soup.title.name)
print("title 태그 문자열: ", soup.title.string)