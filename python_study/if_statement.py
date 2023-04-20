"""
if 조건:
    실행하려는 코드
    코드3줄
    코드4줄
코드4줄
if문은 조건이 True(참)일 때만 안쪽 코드블럭을 실행

if 조건:
    조건이 참일 때 실행하려는 코드
else:
    아닐 때 실행하려는 코드
else는 조건이 False(거짓)일 때 안쪽 코드 블럭을 실행

if 조건1:
    조건1이 True(참)일 때 실행
elif 조건2:
    조건1은 False, 조건2는 True일 때 실행
else:
    조건 1 False 조건 2 False일 때 실행
"""
#bool
#True(참), False(거짓)  첫문자 대문자 유념


# number1 = 6
# number2 = 6
# if number1 > number2:
#     print(number1 > number2)
#     print("number1이 더 크다.")
# elif number1 == number2:
#     print("같다.")
# else:
#     print(number1 > number2)
#     print("number2가 더 크다.")
# 비교 연산자
# a > b   a가 b보다 크다.
# a >= b  a가 b보다 크거나 같다.
# a < b   a가 b보다 작다.
# a <= b  a가 b보다 작거나 같다.
# a == b  a와 b가 같다.
# a != b  a와 b가 같지 않다.

# print (2 > 3) # F
# print (2 >= 3) # F
# print (2 < 3) # T
# print (2 <= 3) # T
# print (2 == 3) # F
# print (2 != 3) # T

# print("a" < "b") #True
# print("CAT" < "cat") #True
# print("COW" > "CAT") #True
# print("DOG" > "dog") #False
# print("DOG" == "dog") #False

#논리 연산자
#George boole (1847) The Mathematical Analysis of Logic
# and: a and b에서 둘다 True일때 True 아니면 False
# or: a or b 형태로 사용 a와 b중 하나라도 True면 True
# not: not a형태로 사용 a가 True면 False로, a가 False면 True로 바꾼다


# print(True and True) #이것만 True
# print(True and False)
# print(False and True)
# print(False and False)


# print(True or True)
# print(True or False)
# print(False or True)
# print(False or False) #이것만 False


# print (not True)
# print (not False)


# age = 17
# if age >= 20:
#     print("축하합니다 성인입니다.")
# money = 10000
# if money >= 10000:
#     print("부자입니다.")

# age = 17
# money = 10000
# if age >= 20 or money >= 10000:
#     print("성인 또는 부자입니다.")
# if age >= 20 and money >= 10000:
#     print("성인이고 부자입니다.")
    
  
if "안녕":
    print("안녕하세요")

if 0:
    print(0)