# 데이터 수집 단계

# 데이터 수집 -> 분석/처리 ->인공지능 모델 학습 ->평가 ->사용

# http (hypertext transfer protocol) - 프로토콜은 약속, 규약
# request - response
# client - server
# html(hypertext markup langauge) 
# 웹사이트를 표현하기 위한 언어
# <html></html>
# 파싱(parsing)- 구문분석
#
# import requests

# url = "https://www.naver.com/"
# response = requests.get(url)
# status = response.status_code
# html = response.text
# print(status) #200 출력
# print(html)

# http 상태 코드
# 200 : OK
# 요청 성공 의미
# 302 : 리다이렉트
# 다른 페이지로 바로 연결
# 400 : Bad Request 요청이 잘못됨
# 401 : Unauthorized 비인증됨
# 403 : Forbidden 접근 권한 없음
# 404 : Not Found 요청받은 내용이 없음
# 405 : Method Not Allowed 접근 방법이 잘못
# 500 : Internal Server Error 서버 에러 (계발자 잘못이 많다)
# 501 : Not Implemented
# 502 : Bad Gateway 잘못된 응답

# url 구조
# 프로토콜://호스트주소:포트번호/경로?쿼리
# http://naver.com/?~~~~~
# 쿼리 : 추가적인 데이터 받을 때 활용, 마치 변수에 데이터 담는 것과 같다
# 쿼리이름=값&쿼리이름=값&쿼리이름=값

# https://search.naver.com/search.naver?where=image&sm=tab_jum&query=%EC%B9%98%ED%82%A8
# query=%EC%B9%98%ED%82%A8 ->쿼리는 치킨
# https://search.naver.com/search.naver?where=image&sm=tab_jum&query=%EC%B9%98%ED%82%A8
# https://search.naver.com/search.naver?where=image&sm=tab_jum&query=%EC%B9%98%ED%82%A8

# import requests
# search_url = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query=%EC%B9%98%ED%82%A8"
# response = requests.get(search_url)
# print(response.text)

#import requests
# search_url = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query= + 맥주"
# response = requests.get(search_url)
# print(response.text)
#


# BeautifulSoup
# html 파싱(parsing)
# html을 객체 구조화해서 사용
# from bs4 import BeautifulSoup
# html 태그
# <태그이름 속성 =속성값>내용</태그이름>
# html = "<html><body>Hello</body></html>"
# soup = BeautifulSoup(html, "html.parser") #bs 객체를 만들어서 soup에 담는다
# import requests
# from bs4 import BeautifulSoup
# search_url = "https://search.naver.com/search.naver?"
# keyword = "맥주"
# url = search_url + keyword
# response = requests.get(url)
# html = response.text
# soup = BeautifulSoup(html, "html.parser")
# print(soup)
# print(type(soup))
# #
# print(soup.body)
# print(type(soup.body))
# # 
# print(soup.body.text)  #Hello 만 가져옴
# print(type(soup.body.text))

# import requests
# from bs4 import BeautifulSoup
# search_url = "https://www.google.co.kr/search?tbm=isch&q="
# keyword = "맥주"
# url = search_url + keyword
# response = requests.get(url)
# # print(response.text)
# html = response.text
# soup = BeautifulSoup(html, "html.parser")
# # print(soup.find_all('div')[5])
# # imgs = soup.find_all('img', attrs={'class': ['_image_listImage']}) #리스트로 표현
# # print(imgs)
# # container = soup.find('div', attrs={'id': 'container'})
# # print(container.find_all('img'))


# import requests
# from bs4 import BeautifulSoup
# search_url = "https://www.google.co.kr/search?tbm=isch&q="
# keyword = "money"
# url = search_url + keyword
# response = requests.get(url)
# # print(response.text)
# html = response.text
# soup = BeautifulSoup(html, "html.parser")
# imgs = soup.find_all('img')
# import os
# folder_name ="imgs"
# if not os.path.exists(folder_name): #폴드이름 없으면 밑을 실행
#     os.mkdir(folder_name) # 폴드 생성 확인

# for idx, img in enumerate(imgs[1:]): #idx는 순번
#     print(idx, "번째 이미지 저장") 
# # print(img)
#     file_name = f"{keyword}_{idx}.jpg"
#     file_path = os.path.join(folder_name, file_name)
#     img_response = requests.get(img['src'])
#     img_data = img_response.content
#     with open(file_path, "wb") as f: #binary로 저장 => wb
#         f.write(img_data)

# # enumerate(이터러블)-번호를 붙이는 기능
# li1 = ["김연아", "류현진", "손흥민"]
# for name in enumerate(li1):
#     print(name)


#연습 네이버 6개 이미지 저장
# import requests
# from bs4 import BeautifulSoup
# search_url = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
# keyword = "money"
# url = search_url + keyword
# response = requests.get(url)
# # print(response.text)
# html = response.text
# soup = BeautifulSoup(html, "html.parser")
# imgs = soup.find_all('img')
# import os
# folder_name ="imgs"
# if not os.path.exists(folder_name): #폴드이름 없으면 밑을 실행
#     os.mkdir(folder_name) # 폴드 생성 확인

# for idx, img in enumerate(imgs[1:]): #idx는 순번
#     print(idx, "번째 이미지 저장") 
# # print(img)
#     file_name = f"{keyword}_{idx}.jpg"
#     file_path = os.path.join(folder_name, file_name)
#     img_response = requests.get(img['src'])
#     img_data = img_response.content
#     with open(file_path, "wb") as f: #binary로 저장 => wb
#         f.write(img_data)

# 네이버 뉴스 기사 a Tag  - 닷
import os
import requests
from bs4 import BeautifulSoup
url ="https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105"
# headers={"User-Agent": "Mozilla/5.0"} --> 크롤링 방지 회피
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
html = response.text
# print(html)
soup =BeautifulSoup(html, "html.parser")
# print(soup.body)
div = soup.body.find('div', attrs={'class': 'list_body'})
# print(div)
headlines = div.find_all('a', attrs={'class':'cluster_text_headline'})
# print(headlines)

folder_name ="crawling_result"
if not os.path.exists(folder_name): #폴드이름 없으면 밑을 실행
    os.mkdir(folder_name) # 폴드 생성 확인
for headline in headlines:   
    print(headline.text.strip())
        
#과제: crawling_result 폴더의 headlines.txt파일에 저장하기
# print(headline.text.strip())
# with open("crawling_result/headlines.txt", "a", encoding="utf-8") as f:
#     f.write(headline.text.strip())
#     f.write("\n")
#     for headline in headlines:

# 기사 및 내용까지 크롤링     
article_response = requests.get(headline['href'])
article_soup = BeautifulSoup(article_response.text, "html. parser")
article = article_soup.find('div', attrs={"id": "dic_area"})
print(article.text)

                       