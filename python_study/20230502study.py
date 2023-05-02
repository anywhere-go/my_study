# def div2(a, b):
#     if a < b:
#       big=b
#       small=a
#     elif b<=a:
#       big=a
#       small=b

#     if small ==0:
#       print('0은 사용할 수 없습니다.')
#     elif abs(big)<0 or abs(small)<0:
#       print('정수를 입력해주세요.')
#     else:
#       q = big//small
#       r = big%small
#       return (q, r)
# div2(3,5)
# div2(20,3)
# 
# def func(string, unit=2):
#   i=0
#   while i<len(string):
#     print(string[i:i+unit])
#     i +=unit
# func('테스트를 위한 문장입니다')


# func('테스트를 위한 문장입니다',5)



# 
# def test(*args):
#   print(args)
# test(1,2,3,4,5)
# test([1,2],8)


# def add_all(*inputs):
#   s=0
#   for i in range(len(inputs)):
#     s +=inputs[i]
#   return s
# add_all(1,2,3)


# def add_all3(*args):
#   s=0
#   for i in args:
#     for j in i:
#       s +=j
#     return s
# add_all3([1,2,3,4,5,6,7,8,9])

#답 45

# def add_all4(*args):
#   temp=0
#   for i in range(len(args)):
#     if type(args[i]) == list:
#       for j in args[i]:
#         temp +=j
#     else:
#       temp +=args[i]
#   return temp

# add_all4([1,2,3,4,5,6,7,8,9,10])
# 답 55


# # 재귀적으로 하지 않은 것
# def fact(n):
#   f=1
#   for i in range(1, n+1):
#     f=f*i
#   return f

# fact(6)
#120

# people =['펭수','뽀로로','뚝딱이','텔레토비']
# def func1(line):
#   new_lines =[]
#   i = 1
#   for x in line:
#       print('대기번호 %d번 : %s' %(i, x))
#       new_lines.append((i,x))
#       i +=1
#   return new_lines

# func1(people)

# 대기번호 1번 : 펭수
# 대기번호 2번 : 뽀로로
# 대기번호 3번 : 뚝딱이
# 대기번호 4번 : 텔레토비
# [(1, '펭수'), (2, '뽀로로'), (3, '뚝딱이'), (4, '텔레토비')]




# people =['펭수','뽀로로','뚝딱이','텔레토비']

# def func1(line):
#   new_lines =[]
#   for idx, val in enumerate(line):
#     print('대기번호 %d번 : %s' %(idx, val))
#     new_lines.append((idx+1,val))
#   return new_lines
# func1(people)

# def plus_two(num):
#   return num +2
# a=2
# b=plus_two(a)
# print(b)
# 4 출력


# lambda x: x+2
# func2 = lambda x: x+2
# c = func2(2)
# c

# items =[1,2,3,4,5]
# squared =[]
# for i in items :
#   squared.append(i*i)

# print(squared)

# squared_map =list(map(lambda x: x**2, items))
# print(squared_map)

# [1, 4, 9, 16, 25]


# items =[1,24,3,6,7]
# str_items =list(map(lambda x:str(x), items))
# print(str_items)
# ['1', '24', '3', '6', '7']


# list_1 =[0,1,2,3,4,5,6,7,8,9]

# list_2 =[]
# for x in range(10):
#   list_2.append(x)
# print(list_2)
# 같은 결과
# lc_1 =[x for x in range(10)]
# print(lc_1)


# tables =[2 *x for x in range(1,10)]
# print(tables)
# [2, 4, 6, 8, 10, 12, 14, 16, 18]



# sentence ="코로나 바이러스를 예방하기 위해 사회적 거리두기를 실천합시다. 외출 시에는 마스크를 끼고 손씻기를 생활화합시다."

# len_sent =[len(s) for s in sentence.split()]
# print(len_sent)
# [3, 5, 4, 2, 3, 5, 6, 2, 3, 4, 2, 4, 7]


# # 10부터 20까지 짝수만 리스트
# list3 =[]
# for x in range(10, 21):
#   if x%2 == 0:
#       list3.append(x)
# print(list3)

# [10, 12, 14, 16, 18, 20]

# lc_2 =[x for x in range(10, 21) if x%2==0]
# print(lc_2)


# # 1부터 10의 제곱수 중 50이하인 수만 리스트 저장
# lc_3=[x**2 for x in range(1,11) if x**2<50]
# print(lc_3)

# [1, 4, 9, 16, 25, 36, 49]


# lc_4=[s for s in sentence.split() if len(s)<5]
# print(lc_4)

# ['코로나', '예방하기', '위해', '사회적', '외출', '시에는', '마스크를', '끼고', '손씻기를']



# # 1부터 10의 숫자들 중 홀수이면 어떤 제곱수를 짝수이면 세제곱수 담은 리스트 
# list_4=[]
# for x in range(1, 11):
#   if x%2 ==1:
#     list_4.append(x**2)
#   else:
#     list_4.append(x**3)
# print(list_4)

# [1, 8, 9, 64, 25, 216, 49, 512, 81, 1000]


# [x**2 if 1%2== 1 else x**3 for x in range(1,11)]



# word1= 'hello'
# word2= 'world'

# result = [i+j for i in word1 for j in word2]
# result


# # for + if 문
# # 40이하 숫자는 5 더하고 40초과 숫자는 41로 바꾸어 리스트 
# [x+5 if x<=40 else x+41 for x in range(1,101)]



# students = {'보라돌이':61,'루비':15,'나나': 78,'뽀':88}

# result =[(name,True) if score>60 else (name, False) for name,score in students.items()]
# result

# [('보라돌이', True), ('루비', False), ('나나', True), ('뽀', True)]


# A = [1,2,3,4]
# a= np.array(A, np.int)
# print(type(a))
# print(a)



# arr = np.array([[1,2,3],[4,5,6]])
# arr2 = np.array([100,200,300])
# arr3= np.array([100,200,400])
# arr+arr3


# list_1=[1,2,3]
# list_1+list_1


# arr.size

# arr.ndim

# arr.shape



# import numpy as np
# a = np.array(10)
# print(a)
# print(a.ndim)

# 10
# 0


# a=np.array([1,2,3])
# print(a)
# print(a.shape)



# a=np.array([[1,2],[3,4]])
# print(a)
# print(a.ndim)


# a=np.array([[[[1,2],[3,4]]]])
# print(a)
# print(a.ndim)
# print(a.shape)



# arr1 = np.array(range(20))
# arr1

# arr2=np.arange(20)
# arr2
# print(arr2.ndim)


# np.empty((2,3),dtype=np.float32)

# np.arange(3,50,3)

# np.arange(-3,3)

# np.linspace(0,1,6)

