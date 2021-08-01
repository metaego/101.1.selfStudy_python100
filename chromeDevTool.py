# 05. 크롬 개발자 도구

# 학습 목표
#: 크롬 개발자 도구를 활용하여 HTML 태그 요소를 확인하는 방법 이해

import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Seoul_Metropolitan_Subway"
resp = requests.get(url)
html_src = resp.text

soup = BeautifulSoup(html_src, 'html.parser')

# find()함수는 처음으로 나타나는 img 태그 부분만 찾아서 출력함
first_img = soup.find(name='img')
print(first_img)
print("\n")

# img 중 원하는 사진을 출력하고 싶다면 아래와 같이 코드 작성
# img 태그 중 속성값이 alt이고 파일명이 Seoul-Metro-2004-20070722.jpg인 것을 찾아서 출력하는 코드
target_img = soup.find(name='img', attrs={'alt':'Seoul-Metro-2004-20070722.jpg'})
print(target_img)