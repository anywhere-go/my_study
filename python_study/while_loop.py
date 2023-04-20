#while 반복문
"""
while 조건:
    반복할 코드
"""
# 조건이 참인 경우에 반복할 코드를 계속 반복한다
# print(1)
# print(2)
# print(3)
# print(4)
# print(5)
# print(6)
# print(7)
# print(8)
# print(9)
# print(10)

# n = 1
# while n <= 1000:
#     print(n)
#     n += 1 # n = n+1

# += 연산자
# 더하기 연산 후 할당
# n += 1은 n = n+1이라는 의미
# -= 
#n -=1은 n =n-1
# *=
# /=
# **=
# //=
# %=

# s1 = "안녕"
# s1 +="하세요"
# s1 = s1 + "하세요"
# print(s1)

#안녕하세요하세요 출력

#while 반복문을 활요
#10부터 1까지 순서대로 출력

# cnt = 10
# while cnt >= 1:
#     print(cnt)
#     cnt -= 1

#똑같은 코드
# cnt = 10
# while cnt > 0:
#     print(cnt)
#     cnt -= 1

# money = 10000
# price = 1000
# coffee = 5
# while money >= price:
# #while money - price >=0:
#     print("커피를 구매했습니다")
#     money -= price
#     coffee -= 1
#     print("남은 커피:", coffee)
#     if coffee == 0:
#         break
#break
#반복문을 즉시 종료한다.
    # if money <= 0:
    #     print("더 이상 커피 살수 없습니다!!")

# prompt = """
# 1. Add
# 2. Del
# 3. List
# 4. Quit

# Enter number:"""

# number = 0
# while number !=4:
#     print(prompt)
#     number = int(input())

#1~10까지 홀수만 출력 while 반복문 활용

# a = 1
# while a <=10:
#     if a % 2 == 1:
#         print (a)
#     a +=1
     
# continue
# 반복문의 제일 처음으로 돌아감 (while문으로 다시 돌아감)


# b = 0
# while b <= 9:
#     b +=1
#     if b % 2 == 1:
#         continue
#     print(b)
    

# b = 0
# while b <= 9:
#     b +=1
#     if b % 2 == 0:
#         continue
#     print(b)


#무한 반복문
# 무한 루프
#조건식에 True를 입력해 항상 참이 되도록 무한 반복
# while True:
#     user_input = input("종료하려면 1을 입력해주세요.")
#     if user_input == "1":
#         break



#무한 반복문으로 계산기 만들기
#+, -,
#a+ b
# while True:
#     print ("""
#         계산기
#     ===============
#     1. 더하기 (+)
#     2. 빼기 (-)
#     3. 곱하기 (*)
#     4. 나누기 (/)
#     """)
#     operator = input ("계산을 선택하세요:")
#     a = int 
#     b = int
#     add = a + b
#     minus = a - b
#     mult = a * b
#     div = a/ b


#     if operator == "1":
#         a = input("숫자를 입력하세요")
#         b = input("숫자를 입력하세요")
#         print(add)
#     if operator == "2":
#         print(minus)
#     if operator == "3":
#         print(mult)
#     if operator == "4":
#         print(div)


# while True:
#     print ("""
#         계산기
#     ===============
#     1. 더하기 (+)
#     2. 빼기 (-)
#     3. 곱하기 (*)
#     4. 나누기 (/)
#     """)
#     operator = input ("계산을 선택하세요:")
#     a = int(input("숫자를 입력하세요."))
#     b = int(input("숫자를 입력하세요."))

#     if operator == "1":
#         print(a, "+", b, "=", a + b)
#     if operator == "2":
#         print(a, "-", b, "=", a - b)
#     if operator == "3":
#         print(a, "*", b, "=", a * b)
#     if operator == "4":
#         print(a, "/", b, "=", a / b)
#     if operator == "q":
#         break

# # 같은 개념으로 if   elif (else + if)도 있다


# while True:
#     print("""
#         계산기
#     ===============
#     1. 더하기 (+)
#     2. 빼기 (-)
#     3. 곱하기 (*)
#     4. 나누기 (/)
#     """)
#     operator = input ("계산을 선택하세요:")
#     a = int(input("숫자를 입력하세요."))
#     b = int(input("숫자를 입력하세요."))

#     if operator == "1":
#         print(a, "+", b, "=", a + b)
#     elif operator == "2":
#         print(a, "-", b, "=", a - b)
#     elif operator == "3":
#         print(a, "*", b, "=", a * b)
#     elif operator == "4":
#         print(a, "/", b, "=", a / b)
#     if operator == "q":
#         break



#     a = 1
#     if a == 2:
#         print(2)
#     else:
#         if a == 3:
#             print(3)
#         else:
#             print(1)

#     a = 1
#     if a == 2:
#         print(2)
#     elif a == 3:
#         print(3)
#     else:
#         print(1)


#사용자가 가지고 있는 돈을 입력
#총 몇 개의 커피를 구매할 수 있는 커피 개수와 잔돈 출력
#몇 개의 음료수를 구매할 수 있는지와 잔돈 출력
#구매할 수 있는 콜라의 개수와 잔돈을 출력
#커피는 500원 음료수는 700 콜라는 930원
#물품의 개수는 무한하다고 가정
#While 반복문 사용 작성


# idx = 0
# prices = [500, 700, 930]
# money = int(input("돈:"))
# while idx < len(prices):
# #while idx <=2:
# #while idx <3:
#     price = prices[idx]
#     print(money // price)
#     print(money % price)
#     idx += 1


#while 반복문 
#scores 리스트에 시험 점수 5개를 정수형으로 입력받으세요.

# idx = 0
# a = int(input("시험과목1:"))
# b = int(input("시험과목2:"))
# c = int(input("시험과목3:"))
# d = int(input("시험과목4:"))
# e = int(input("시험과목5:"))
# scores = int(input([a,b,c,d,e]))
# while idx < len(scores):
#     score = scores[idx]
#     print(score)
#     idx += 1

#강사 코드 마지막에 스코어 출력
# scores = []
# n = 0
# while n < 5:
#     score = int(input("시험점수:"))
#     scores.append(scores)
#     n += 1
# print(scores)

#입력 될때마다 스코어 출력하기
# scores = []
# n = 0
# while n < 5:
#     score = int(input("시험점수:"))
#     scores.append(scores)
#     n += 1
#     print(scores)


#while 반복 구구단 2단 출력

# a = 2
# b = 1
# while b <10:
#     print(a*b)
#     b +=1


# n = 1
# while n < 10:
#     print("2 *", n, "=", 2*n)
#     n +=1


#파이썬 구구단 출력하기 검색
# print("★ 구구단을 출력합니다.\n")
# for x in range(2, 10):
#     print("------- [" + str(x) + "단] -------")
#     for y in range(1, 10):
#         print(x, "X", y, "=", x*y)
# print("---------------------")

