# 06. 웹 문서의 그림 이미지 파일을 PC에 저장하기 

# 학습 내용
# : 웹 문서에서 그림 이미지를 선택하여 사용자 PC에 저장한다

from bs4.element import SoupStrainer
import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Seoul_Metropolitan_Subway"
resp = requests.get(url)
html_src = resp.text

soup = BeautifulSoup(html_src, 'html.parser')

target_img = soup.find(name='img', attrs={'alt':'Seoul-Metro-2004-20070722.jpg'})
print('HTML 요소:', target_img)
print('\n')

target_img_src = target_img.get('src')
print('이미지 파일 경로:', target_img_src)
print("\n")

# 추출한 이미지 파일 경로에 http:를 보완하고 request의 get()함수를 적용
# 이미지 파일 경로에 get 요청을 보내면 이미지 파일을 담은 응답 객체를 target_img_resp 변수에 저장
target_img_resp = requests.get('http:' + target_img_src)
out_file_path = "./output/download_image.jpg"

# target_img_resp 변수에 저장된 request 응답 객체의 content 속성에는 이미지 파일이 바이너리 형태로 저장되어 있음
# write 명령으로 저장 위치를 지정하여 외부 파일로 저장
# (파일 열때) wb : write + binary
with open(out_file_path, 'wb') as out_file:
    out_file.write(target_img_resp.content)
    print("이미지 파일로 저장하였습니다")