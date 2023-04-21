#2~9사이 숫자 입력받아
#해당하는 단의 구구단을 출력
#2~9사이 숫자 아닌 값 입력, 잘못 입력되었다고 출력 다시 입력

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

# numbers = []
# number = int(input("숫자 입력:"))
# for i in range (2, 10):
#     for j in range (1, 10):
#             print (i, "*", j, "=", i*j)
#     if number == i:
#             print (i, "단\n")

    
#

# # 2~9 사이의 값이 아닐 때 True
# if n < 2 or n > 10:
#     print("입력을 다시 하시기 바랍니다")
# # if n < 2 or n > 10:
# if n >= 2 and n <= 9:
#     pass
# if 2 <= n <=9:
#     pass
#     #구구단 출력하는 코드
# n = int(input("몇 단?"))
# while not 2 <= n <=9:
#     print("2~9 사이의 숫자를 입력해주세요")
#     n = int(input("몇 단?")) 
# for i in range(1, 10):
#     print(n, "*", i, "=", n*i)
#for i in range(9):
#     print(n *(i+1))


#정수를 입력받고
# 그 정수보다 작은 수 중
# 가장 큰 제곱수를 출력


# n = int(input ("숫자 정수:"))
# i = 1
# while True:
#     # i*i
#     if i ** 2 >= n:
#         break
#     answer = i**2
#     i += 1
# print(answer)

# [1, 2, 3, 4, 5]
# [10, 20, 30, 40, 50]
# [532, 5941, 54682, 58, 5]
#같은 인덱스의 값끼리 더하여 출력하세요
# li_1 = [1, 2, 3, 4, 5]
# li_2 = [10, 20, 30, 40, 50]
# li_3 = [532, 5941, 54682, 58, 5]
# for i in range(5):
#     print(li_1[i] + li_2[i]+li_3[i])

#zip()
#길이가 같은 List를 묶어서 for문 등으로
#사용가능한 iterable을 반환한다.

# for x, y, z in zip(li_1, li_2, li_3):
#     print(x + y + z)


# li_1 = [1, 2, 3, 4, 5]
# li_2 = [10, 20, 30, 40, 50]
# li_3 = [532, 5941, 54682, 58, 5]
# i=0
# while i < 5:
#     print(li_1[i] + li_2[i]+li_3[i])
#     i +=1


#정수를 입력받고 1부터 입력받은 정수까지 모두 출력하세요.
#단, 숫자에 3, 6, 9가 들어있는 경우 숫자 대신 짝이라고 출력

# n = int(input("정수:"))
# for i in range(n):
#     answer = i +1
#     if answer == 3:
#         print("짝")
#     print(answer)

# n = int(input("정수:"))

# for i in range(1, n+1):
#     #3,6,9들어있으면
#     for j in str(i):
#         if int(j)% 3 ==0:
#             print("짝")
#             continue
#     print(i)
#for in in range(1, n+1):
# print(i)
#931 //100
# 931%100
# 31//10 == (931 % 100) // 10  


# n = int(input("정수:"))

# for i in range(1, n+1):
#     answer = i
#     #3,6,9들어있으면
#     for j in str(i):
#         if int(j)% 3 ==0 and j !="0":
#             answer ="짝"
#             break
#     print(answer)


#약수: 나누었을 때 나머지가 0으로 나누어 떨어지게 하는 수
# n = int(input("정수: "))
# for i in range(1, n+1):
#     if n % i == 0:
#         print(i,"(은)는 약수이다")


# n = int(input("정수: "))
# for i in range(n):
#     if n % (i+1) == 0:
#         print(i+1,"(은)는 약수이다")

# #똑같은 While 문 코드
# i = 1
# while i <= n:
#     if n % i == 0:
#         print(i)
#     i += 1