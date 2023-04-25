# 파일 입출력
# 파이썬에서 파일 생성, 수정
# open()
# 파이썬 내장함수
# 파일을 열고, 파일 객체를 리턴한다
# open(파일 이름, 파일 열기 모드) 형식을 사용한다
# f = open("C:/Users/405/my_study/python_study/새파일.txt", 'w')
# f.close()
# 파일의 경로 2가지
# 절대 경로: C:/ D:/처럼 최상단 경로부터 나타낸 경로
# 상대 경로: 현재 작업 위치부터 나타낸 경로

# 파일 열기 모드
# r: 읽기 모드, 파일을 읽기만 할 때 사용
# w: 쓰기 모드, 파일에 내용을 쓸 때 사용
# a: 추가 모드, 파일의 마지막에 새로운 내용을 추가할 때 사용

# f = open("python_study/새파일.txt", 'w', encoding="utf-8")
# for i in range(1, 11): #1~10
#     print(i, "번째 줄")
#     f.write(str(i)+"번째 줄\n")#\n추가하면 줄바꿈이 된다
# f.close()
# w모드는 덮어쓰기 된다. 기존 파일내용이 사라진다.


# a모드사용
# f = open("python_study/새파일.txt", 'a', encoding="utf-8")
# for i in range(11, 21): #11~20
#      print(i, "번째 줄")
#      f.write(str(i)+"번째 줄\n") 
# f.close()

# f = open("python_study/새파일.txt", 'r', encoding="utf-8")
# readline()함수
# 첫번째 줄부터 1줄 읽어온다.
# 커서가 이동하는 것처럼 읽어옴
# while True:
#     line = f.readline()
#     if line =="":
#         break
#     print(line)
# f.close()

# 1번줄 2번줄 출력하기
# line = f.readline()
# print(line)
# line = f.readline()
# print(line)

# readlines()함수
# lines = f.readlines()
# print(lines)
# f.close()
#

# lines = f.readlines()
# for line in lines:
#     print(lines) #lines
# f.close()
# #

# lines = f.readlines()
# for line in lines:
#     print(line) #line
# f.close()


#read()함수 ---1~20줄 연속출력
# f = open("python_study/새파일.txt", 'r', encoding="utf-8")
# data =f.read()
# print(data)
# f.close

#for문으로 읽기
# f = open("python_study/새파일.txt", 'r', encoding="utf-8")
# for line in f:
#     print(line)
# f.close

#with 문
#open -close를 자동으로 해준다
# with open("python_study/새파일", "a", encoding = "utf-8") as f:
#     f.write("end of file")
#     f.write("2")
#     f.write("2")
#     f.write("2")
# f.write("5")  # 이것은 실행이 안됨- 에러발생함
#
#close 자동으로 해주는 구문 -실행결과 end of file234
# with open("python_study/새파일.txt", "a", encoding = "utf-8") as f:
#     f.write("end of file")
#     f.write("2")
#     f.write("3")
#     f.write("4")

# csv(comma separated values)
# ,로 구분되는 값들을 모아놓은 파일- 출결데이터
# 이름,입실시간,퇴실시간
# 권오천,09:20,18:10
# 김예진,09:21,18:11

# csv(comma separated values)
# ,로 구분되는 값들을 모아놓은 파일
# with open("python_study/data.csv", 'w', encoding="utf-8") as f:
#     f.write("날짜,날씨,기온\n")
#     f.write("20230424,맑음,10\n")
#     f.write("20230425,비,9\n")


# with open("python_study/data.csv", 'r', encoding="utf-8") as f:
#     data = f.readlines()
#     print(data)


#계산 결과 저장 함수
#정수 2개 입력받고
#두 수를 더한 결과를 add_result.txt파일에 저장하는 함수를 정의하세요.
#함수 이름: add_write

# def add_write(a, b):
#     # a + b --> write
#     result = a + b


#     with open("python_study/add_result.txt", 'a',encoding="utf-8") as f:
#          f.write(str(result))
# add_write(1, 2)


#텍스트 파일에 적힌 정수 2개를 읽어와서 더하는 함수를 정의하세요
#텍스트 파일 이름: add_number.txt
#경로: python_study/add_number.txt
#정수 2개를 더한 결과를 print하세요
#함수 이름: read_add_print

# def read_add_print():
#     with open("python_study/add_number.txt", 'r', encoding="utf-8") as f:
#         data = f.read() #문자열 모두 읽어서 data에 저장
#         a = int(data[0]) #문자열을 정수형으로 바꾸어야 한다
#         b = int(data[2])
#         print(a+b)

# read_add_print()

#실행결과 3이 출력 (1 2)


#사칙연산 계산기 만들기
# n1 = int(input('첫번째 숫자를 입력하세요:'))
# op = input('연산자를 입력하세요:')
# n2 = int(input('두번째 숫자를 입력하세요:'))
# if op =='+':
#     print(n1 + n2)
# elif op == '-':
#     print(n1 - n2)
# elif op == '*':
#     print(n1 * n2)
# elif op == '/':
#     if n2 == 0:
#         print('0으로 나눌 수 없습니다')
#     else:
#         print(n1 / n2)
# else:
#     print('잘못 입력하셨습니다')
    


#계산기 만들기
#기능:
#add(), sub(), mul(), div() 함수 정의
#input() 함수 활용
#정수 2개, 사칙연산 선택을 입력받은 후
#계산 결과를 print한다.
#계산식과 결과를 calculator_result.txt파일에 저장 기록한다
#사용자가 'q'를 입력하면 종료한다

# def add(a, b):
#     # a + b --> write
#     result = a + b


#     with open("python_study/calculator_result.txt", 'a',encoding="utf-8") as f:
#          f.write(str(result))

# add_write(1, 2)