# 정육면체 주사위 2개가 있다.
# 2개의 주사위를 던졌을 때 나올 수 있는 주사위 눈의 조합을 모두 print하는 함수를 정의
# 함수 이름: double_dice
# 출력 예시
# 1, 2
# 6, 3

# def double_dice():
#     for i in range(1,7):#1~6
#         for j in range(1,7):#1~6
#             print(i,j)

# double_dice()

# # while 문으로 변경
# i = 1
# while i < 7:
#     j = 1
#     while j < 7:
#         print(i, j)
#         j += 1
#     i += 1

#문제
#두 수의 차이를 구하는 함수
#함수에 입력된 두 정수의 차이를 계산하고 반환하는 함수를 정의하세요
#함수 이름: get_diff

# def get_diff(a, b):
#     result = abs(a- b)
#     return result
# print(get_diff(10,2))
# # 똑같은 것
# def get_diff(a, b):
#     result = abs(a- b)
#     if a > b:
#         result = a -b
#     else:
#         result = b - a
#     return result
# print(get_diff(10,2))


#가장 큰 수를 만드는 함수
#함수에 입력된 5개 정수를 사용하여 만들 수 있는 가장 큰 수를 반환하는 함수를 정의
#
#함수 이름: get_biggest

# def get_biggest(a, b, c, d, e):
#     numbers = [a, b, c, d, e]
#     numbers.sort()
#     result = 0
#     for i in range(len(numbers)): #0~4
#         result += numbers[i]*(10**i)
#     return result


##똑같음
    # numbers = [a, b, c, d, e]
    # numbers.sort(reverse=True)
    # result =""
    # for i in numbers:
    #     result += str(i)
    # return int(result)

#별 찍기2
#정수를 함수에 입력하여 호출하면 해당 정수 줄의 별을 화면에 출력
#함수 이름: print_stars2
#    *
#   **
#  ***
# ****

# def print_stars2(n):
#     for i in range(1, n+1):
#         print("" * (n - i) + "*" * i) #""사이 공백이 없으면 왼쪽부터 별, 공백이 있으면 오른쪽부터 별


# print_stars2(4)

def print_stars2(n):
    for i in range(1, n+1):
        print(" " * (n - i) + "*" * i) #""사이 공백이 없으면 왼쪽부터 별, 공백이 있으면 오른쪽부터 별


print_stars2(19)