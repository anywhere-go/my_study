# function 함수
# 입력 -> 처리 -> 출력
# input(입력)을 받아서 특정 작업(처리)을 수행하고 output(출력)을 반환한다.

# 내장 함수 (built-in function) 종류
# 파이썬이 기본적으로 제공해주는 함수
# print()
# len()
# zin()
# int()
# float()
# str()
# list()
# range()

# abs()
# absolute의 약자
# 입력한 숫자형 데이터의 절대값을 반환한다
# 100의 절대값
# print(abs(100))
# print(abs(-100))
# print(abs(3.15))
# print(abs(-3.15))    


# sum(리스트)
# 리스트 안의 숫자를 더한 값을 반환한다
# print(sum([1,2,3,4,5]*2))


# max(리스트)
# 리스트 안에서 최댓값을 찾아 반환한다.
# print(max([1, 2, 3, 400, 5, 100]))


# min(리스트)
# 리스트 안에서 최솟값을 찾아 반환한다
# print(min([1, 2, 3, 400, 5, 100]))


# chr(정수)
# 정수 1개를 입력받고 해당하는 유니코드 문자를 반환한다
# print(chr(65)) # 알파벳 A가 출력

# ord(문자)
# 문자 1개를 입력받고 해당하는 정수를 반환한다.
# print(ord('A'))

# round(값)
# 반올림 함수
# 사용법은 2가지 rount(값) 또는 rount(값, 소수 자릿수)
# print(round(1.234))  # 1
# print(round(1.234, 2)) # 1.23
# print(round(1.369,1)) #1.4

# 함수 정의(define)
# 함수 이름 (변수 이름처럼 규칙을 지켜서 만듬- 영어, 숫자, _ 등으로 사용)
# 숫자로 시작하면 안됨, 띄어쓰기하면 안됨, 키워드 사용하면 안됨
# 기존에 이미 정의된 함수 이름도 피하는 것이 좋다. 왜냐하면 덮어쓰기 하기 때문에 문제 발생
# 함수 입력값 parameter(매개변수, argument혼용)
# 함수 결과값 return value
"""
def 함수이름(함수입력값):
    함수기능코드
    return 함수 결과값
"""
# def는 함수를 정의하는 명령어로써 define에서 유래
# 입력값과 return값이 없는 함수 예- 출력만 하고 바로 종료. 
# def print_names():
#     print("손흥민")
#     print("황희찬")
#     print("김민재")
#     print("이강인")

# print_names()

# def get_name():
#     return "이재우"  # 결과값(반환값)이 있어서 변수로 활용할 수 있다

# def print_my_name():
#     print(get_name())

# print_my_name()
# a = print_my_name() #리턴값이 없음, None(없다의 의미)
# b = get_name() #리턴값이 있음 그래서 리턴값을 변수에 넣을 수 있다
# print(a)  #a = None이 들어감
# print(b)


# def add(a, b):
#     return a + b # 밑에 있는 구문가 다른점은 return값이 있다

# def print_add(a, b):
#     print(a + b)

# result = add(1, 2) 
# print(result)


# #print_add(1, 2)
# result = print_add(1, 2) #이미 3이 출력되고 다시 부르면 값이 없는 none으로 출력됨
# print(result)


# print_add("안녕", "하세요")  #안녕하세요 출력되지만  ("안녕", 1)은 에러가 나옴(문자 +숫자 불가능)
# print_add("하세요", "안녕")  #하세요안녕이 출력되므로 순서, 위치가 중요함

# print_add(b = "하세요", a="안녕")

# def swap_number(a, b): # 함수,if, for문 안에서의 변수 (지역변수=로컬변수)
#     temp = a
#     a = b
#     b = temp
#     print(a, b)
# # swap_number(1,2)

# a = 1  # 함수 밖에서의 변수 (전역변수=글로벌변수)
# b = 2
# print("함수 호출 전", a, b)
# swap_number(a, b)   #지역변수 출력
# print("함수 호출 후", a, b) # 전역변수 출력



# def swap_number(a, b): # 함수,if, for문 안에서의 변수 (지역변수=로컬변수)
#     temp = a
#     a = b
#     b = temp
#     print(a, b)
#     return a, b   #지역변수 값 전역변수에 출력하기 위해 return 활용

# a = 1  # 함수 밖에서의 변수 (전역변수=글로벌변수)
# b = 2
# print("함수 호출 전", a, b)
# a, b= swap_number(a, b)   #지역변수값을 전역변수에게 넘김
# print("함수 호출 후", a, b) # 전역변수 출력


#다음 함수를 정의하세요
#함수 이름: mul
#함수 입력값: 정수 2개
#함수 출력값: 정수 2개의 곱

# def mul(a, b):
#     return a* b
# result = mul(3, 3)    
# print(result)


# def mul(n1, n2):
#     return n1* n2
# result = mul(3, 3)    
# print(result)
# #똑같음
# def mul(n1, n2):
#     return n1* n2
# print(mul(3, 3))    



# 기본값 매개변수
# default value parameter
# 함수 호출 시 n2에 입력된 값이 없으면 기본값 사용
# def mul(n1, n2=1): 
#     return n1 * n2

# print(mul(1, 2)) #2 출력
# print(mul(1)) #1 출력


# def test_func(x, test=[]):#리스트 형식 사용하면 안됨
#     test.append(x)
#     print(x, test)

# test_func(1)
# test_func(2)  # 기본값으로 list사용하면 계속 누적되어 결과 출력되므로 기본값으로 list 사용 금지



# def test_func1(x, test=5):
#     test = test
#     print(x, test)

# test_func1(1)
# test_func1(2) 


# def test_func2(x, test=None):
#     if test == None:
#         test =[] #비어있는 리스트 만듬
#     test.append(x)
#     print(x, test)

# 기본값이 있는 매개변수는 기본값이 없는 매개변수보다 뒤에 위치해야 함
# def sub(n1, n2, n3=0):
#     print(n1 - n2 - n3)


# def sub(n1, n3, n2=0):
#     print(n1 - n2 - n3)

# def sub(n1, n2=0, n3): #에러 발생
#     print(n1 - n2 - n3)

#1~10까지 더한다
#*를 사용한 매개변수
#입력값이 몇개가 될지 모를 때(안 정해졌을 때) 사용하는 방버
# def add_many(*args):
#     #튜플처럼 사용한다(수정 불가능)
#     #인덱싱, 슬라이싱, for문 사용 가능
#     result = 0
#     for i in args:
#         result += i
#     return result


# result1 = add_many(1,2,3,4,5)
# print(result1)
# result2 = add_many(3,2,5,9, 1)
# print(result2)
# result3 = add_many(1, 2)
# print(result3)


# def calc_many(n1, *args):
#     result = n1
#     for i in args:
#         result += i
#     return n1



#키워드 매개변수
# **Kwargs -- keyword arguments의 줄임말
#딕셔너리로 사용-- 값과 value로 구성
# def print_kwargs(**kwargs):# 값이 유동적으로 많이 들어올 때 사용
#     print(kwargs)

# print_kwargs(a=1, b=2)
# print_kwargs(name="이름",age =10)


#함수의 반환
# return 반환값
# return을 만나면 반환값을 반환함과 동시에 함수가 종료된다.

# def test_func5():
#     print(1)
#     Print(2)
#     print(3)
#     print(4)
#     return None   #return 만나서 함수가 종료되어 print(5)실행 안됨, return 옆에 None은 1개여야 함
#     print(5)

#함수의 반환값은 무조건 1개이다.
# def test_func6(a, b):
#     return a + b
#     return a* b #return 2개 에러 발생 
#     # return a + b, a * b # return (a + b, a * b)

#해결방법
# def test_func6(a, b):
#     return a + b, a * b  #이렇게 사용해야 된다. return 2개 안됨
# result = test_func6(1, 2) #통으로 결과값 저장 -> (3, 2)
# res_add, res_mul = test_func6(1,2) #까서 각각 저장 ->3 2

# # res_add, res_mul = (a + b, a*b)
# print(result)
# print(res_add, res_mul)


# 홀수 판별 함수
# 정수 1개 입력받고 홀수인지 판별하는 함수
# 함수 이름 : is_odd_number
# 파라미터: n
# 반환값: 홀수면 True, 짝수면 False


# def is_odd_number(n):
#     if n % 2 == 1:
#         return True
#     else:
#         return False
    
# print(is_odd_number(5))


# def is_odd_number(n):
#     if n % 2 == 1:
#         return True
#     return False

# is_odd_number(10)
# 더 간단하게는
# def is_odd_number(n):
#     return n%2 == 1


#테두리 출력하는 함수(*****)
#문자열 입력받고 print 함수 이용해 테두리와 함께 문자를 출력
#함수 이름: get_bordered_str
#파라미터: messae
#반환값: None
#print 예시

#*****
#hello
#*****

# def get_bordered_str(message):
#     n = len(message) # 
#     print("*" * n)
#     print(message)
#     print("*" *n)
# get_bordered_str("memory king")
# get_bordered_str(str(12345)) #숫자만 넣으면 error 앞에 str붙여서 문자화 함 len은 연결형 데이터
# #
# def get_bordered_str(message):
#     message = str(message)
#     n = len(message) # 
#     print("*" * n)
#     print(message)
#     print("*" *n)
# get_bordered_str("memory king")
# get_bordered_str(12345) #숫자만 넣으면 error 앞에 str붙여서 문자화 함 len은 연결형 데이터
# #




#리스트형 자료 합계, 평균구하기
# def get_sum_average(arg):
#     length = len(arg)
#     if length == 0:
#         return "요소의 개수가 0 입니다."
    
#     total = 0
#     for x in arg:
#         total = total + x
#     return {"합계": total, "평균": total / length}

# print(get_sum_average([]))
# print(get_sum_average([3,2]))
# print(get_sum_average([-1, 0, 1, 2, 3]))


#전화번호 뒷 4자리 ****로 변환하기
# def replace_digits(str_):
#     return str_[:9] + "****"

# print(replace_digits("010-1234-5678"))
# print(replace_digits("010-9876-5432"))


# 속도를 변환하는 함수
# m/s 단위의 속도가 입력되면
#km/h단위의 속도로 변환
#함수 이름: convert_velocity
#파라미터: velocity
#반환값: km/h로 변환된 속도

# def convert_velocity(velocity):
#     #1m/s *3600 /1000 ==> 3.6km/h 
#     #초속 * 3600/ 1000 ==>시속
#     #초속 * 3.6 = 시속
#     result = velocity * 3.6
#     return result
# velocity = convert_velocity(10)
# print(velocity)


"""
출력결과 n ->4
* 
**
***
****
"""

#별 찍기 함수
# 정수를 함수에 입력하여 호출하면 해당 정수 줄의 별을 화면에 출력한다
#함수이름: print_stars
#파라미터: n
#반환값: None




# def print_stars(n):
#         # 첫번째
#         for i in range(n+1):
#             print(print_stars("*" *(i)))

# 다이아몬드 (정방향 + 역방향)

# for i in range(6): # 정방향
#     print(' ' * (5 - i) + '*' * (i * 2 + 1))
# for i in range(6): # 역방향
#     print(' ' * i + '*' * (11 - (2 * i)))

# 출력 결과
#      *
#     ***
#    *****
#   *******
#  *********
# ***********
# ***********
#  *********
#   *******
#    *****
#     ***
#      *



# n = int(input('n : '))
# for i in range(1,n+1):
#     print('*'*i)
# n = 3 일때,
# '''
# *
# **
# ***
# '''

# def print_stars(n):
#     for i in range(n): #0~n-1
#         for j in range(i+ 1): #0~i
#             print("*", end="")
#         print() #아무것도 출력안하고 줄바꿈만 일어남

# print_stars(4)

# #
# def print_stars(n):
#     for i in range(0, n+1): #0~n-1
#         print(i * "*")
# print_stars(4)


    # for i in range(n):
    #     print("*" *(i +1))


# i = 0
# while i < n:
#     j = 0
#     while j < i +1:
#         print("*", end="")
#         j +=1
#     print()
#     i += 1
# print_stars(4)


#다음 함수를 정의하세요.
#정수 n을 입력받고, n보다 작은 수 중 3의 배수와 5의 배수를 모두 더한 합을 반환하는 함수
#함수 이름: sum_3_5

# def sum_3_5(n):
#     for i in range(0,i+1,3):
#         if i % 3 == 0 and i <=n:
#             print(i)
#     for j in range

    
#     return sum_3_5(sum(i+j))

# 강사 풀이
def sum_3_5(n):
    result = 0
    for i in range(1,n):
        if i % 3 == 0 or i % 5 == 0:
            result += i
    return result

print("\n")
print(sum_3_5(9))
# 고쳐야 할 부분? 뒤에 if를 elif로 바꿔주면 된다
# def sum_3_5(n):
#     result = 0
#     for i in range(n):
#         if i % 3 == 0:
#             result += i
#         if i % 5 == 0:
#             result += i
#     return result


