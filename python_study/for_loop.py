#for 문
# print("★ 구구단을 출력합니다.\n")
# for x in range(2, 20):
#     print("------- [" + str(x) + "단] -------")
#     for y in range(1, 20):
#         print(x, "X", y, "=", x*y)
# print("---------------------")

"""
for 변수 in iterable값:
    반복할 코드
"""
#iterable 순회가능하다  문자, 숫자
# li_1 =["one", "two", "Three"]
# for i in li_1:
#     print(i)
#첫번째 요소부터 마지막 요소까지
#변수에 대입하면서 반복

#문자열 예시
# s1 = "hello World"
# for i in s1:
#     print(i)

#while 과 for 차이는 무한반복이 되느냐 아니냐

# numbers = [1,2,3,4,5,6,7,8,9,10]
# for number in numbers:
#     print(number)
# numbers.reverse()
# print(numbers.reverse)

# numbers.reverse()
# print(number)

#range()
#숫자 range 객체를 만들어 주는 함수
#range(끝 정수)
#0~끝 정수 - 1
#range(시작, 끝)
#시작 ~끝 -1
#range(시작, 끝, 스텝)
#시작 ~끝 -1 까지인데 스텝만큼 차이나게


# for i in range(10): #0~9까지
#     print(i)

# for i in range(1, 11):#1~10
#     print(i)

# for i in range(1,21,3):
#     print(i)

#문제 for 문 사용 2부터 30까지 출력

# for i in range (2,31):
#     print(i)

# #2부터 30까지 숫자 중 짝수만 출력
# for i in range(2, 31): #2~30
#     if i % 2 == 1: #홀수
#         #continue
#         pass # 아무것도 안하고 그냥 넘어갈 때
#     else: #짝수
#         print(i)
#     print("반복")

# #다른 코드
# for i in range (2, 31):
#     if i %2 ==0: #작수
#         print(i)

# if 1 == 1:
#     pass  #동작이 아직 안 정하거나, 아무런 동작 안할 때 넘어간다
# print("완료")

# for i in range(5):
#     pass
# print("완료")

# # for j in range (2, 31, 2): #2~30까지 2씩 차이나는 범위
# #     print(j)
# #문제 for 문을 사용하여 10부터 1까지 출력)
# for i in range (10, 0, -1):
#     print (i)

# for i in reversed(range(1, 11)):
#     print(i)

# for i in range(1, 11)[::-1]:
#     print(i)
# 슬라이싱 [시작인덱스:끝인덱스:방향]
#역방향 = -1

# for i in range (10):
#     if i % 2 == 0:
#         continue
#     print(i)

# money = 10000
# price = 1000
# coffee = 5
# for i in range(coffee): #0~4
#     print("커피를 구매했습니다.")
#     money -= price # money = money - price
#     print("남은 커피 :", coffee -1 -i )
#     if money < price:
#         break


# for i in range(1, coffee +1):#1~5
#     print("남은 커피:", coffee -i) 

# for i in range(coffee):
#     coffee -=1 # coffee = coffee-1
#     print("남은 커피:", coffee) #4~0


#음료수 가격 for 문
# prices = [500, 700, 930]
# money = int(input("가진 돈:"))
# for i in range(len(prices)): #i 0~2 len 3
#     price = prices[i]
#     print(money // price)
#     print(money % price)
# for price in prices:
#     print(money // price)
#     print(money % price)


# scores = []   
# for i in range(5):
#     score = int(input("시험 점수: "))
#     scores.append(score)


#구구단 2단
# for i in range (1, 10): #1~9
#     print("2*", i, "=", 2*i)

#이중 for 문
# for i in range (2, 10): #2~9
#     print(i, "단\n" )
#     for j in range(1, 10):
#         print (i, "*", j, "=", i*j)
#     print("----------\n\n")


# words =["혼자", "공부하는", "첫", "프로그래밍", "!"]
# for x in words:
#     if x == "첫":
#         print("첫 프로그래밍 축하합니다!")
#         break
#     print(x)
#혼자
#공부하는
#첫 프로그래밍 축하합니다!

#
count = range(20)
for x in count:
    if (())