"""
eng 변수, kor 변수, math 변수를 만들고 각 변수는 과목의 시험 점수이다.
영어점수는 80
국어는 60
수학 50점
3과목 점수의 평균을 내고
평균 점수에 따라 성적을 출력한다.
A: 91~100
B: 81~90
C: 71~80
D: 61~70
F: 60이하
"""


eng = int(input("영어 점수"))
kor = int(input("국어 점수"))
math = int(input("수학 점수"))
avg = (eng+kor+math)/3
if avg >= 91:
    print("A학점 축하드립니다!")
elif avg >=81:
    print("B학점 입니다!")
elif avg >=71:
    print('C학점 입니다!')
elif avg >=61:
    print("D학점 입니다!")
else :
    print("안타깝지만 F학점 입니다!")


# input() 함수
# 사용자로 부터 정보를 입력받는 함수
# user_input = input()
# print(user_input)
# 정수형 변환 함수
# 정수형, integer형, int