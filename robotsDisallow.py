# 03. 로봇 배제 표준
# 로봇 재체 표준이란 웹 사이트에 로봇이 접근하는 것을 방지하기 위한 규약을 의미.
# 일반적으로 접근 제한에 대한 설명을 rogots.txt에 기술

# 대부분의 사이트들이 웹 크롤링 로봇의 접근 권한에 대해 설정하고 있기 떄문에
# 웹 페이지에 접근하기 전에 반드시 로봇 배제 표준을 확인하고 가이드라인을 준수해야 할 필요가 있다
# robots.txt 파일을 확인하는 방법은 해당 홈페이지url/robots.txt라고 입력


# requests 모듈을 사용하여 robots.txt 확인하기
import requests

urls = ["https://www.naver.com/", "https://www.python.org/"]
filename = "robots.txt"

for url in urls:
    file_path = url + filename
    print(file_path)

    resp = requests.get(file_path)
    print(resp.text)
    print("\n") 