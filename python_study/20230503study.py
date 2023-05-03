# #args 를 input으로 받기 함수
# def add_all(*inputs):
#   s=0
#   for i in range(len(inputs)):
#     s +=inputs[i]
#   return s
# add_all(1,2,3,4,5,6,7,8,9,10,100)


# import numpy as np
# A =[1,2,3,4]
# a = np.array(A)
# s=a[:2]
# print('A의 출력입니다.%a' %a)
# print('s의 출력입니다.%s' %s)


# type(A)
# type(a)

# ss = a[:2].copy()
# print(ss.size)
# ss[0]=99
# print(a)
# print(s)
# print(ss)


# arr = np.array([[1,2,3],[4,5,6]])
# arr / arr

# arr = np.array([[1,2,3],[4,5,6]])
# arr4= np.array([[1,2,3],[4,5,6]])
# arr + arr4

# arr = np.zeros((3,2))
# arr

# arr.flatten()

# arr = np.array([[1,2],[3,4]])
# arr.flatten()

# #reshappe
# #이미 존재하는 배열을 내가 원하는 대로 shape조정
# arr = np.arange(12)
# arr

# arr.reshape(3,4)
# arr.reshape(1,12) #=flatten()
# arr.reshape(12,1)
# arr.reshape(2,6)


# arr = np.arange(20)
# arr
# arr.reshape(1,20)

# arr.reshape(-1,5)

# arr.reshape(5,-1)
# #
# #
# arr = np.arange(20).reshape(4,5)
# arr

# print(arr.transpose().shape)
# arr.transpose()
# arr1 = arr.transpose()
# arr1

# A = [5,23,2,1,5]
# A.sort()
# A

# a1= [5,23,2,1,5]
# sorted(a1)
# a1

# arr = np.arange(30).reshape(3,2,5)
# arr.shape
# #
# #
# arr.transpose().shape  #축을 건더리기 때문에 3차원에서는 안 쓴다

# arr.T

# x = np.arange(6).reshape(-1,3)
# x


# x.T

# arr=np.arange(21)
# arr1 =[]
# arr2=[]
# for i in arr:
#   if arr[i]%2==0:
#     arr1.append(arr[i])
#   else:
#     arr2.append(arr[i])
# print(arr1)
# print(arr2)

# import numpy as np
# Arr =np.arange(0,21)

# Arr1 =Arr[Arr%2==0]
# Arr2 =Arr[Arr%2!=0]
# print(Arr1)
# print(Arr2)
# print(Arr%2==0)

# arr1d = np.arange(8)
# arr1d[1]

# arr1d[-1]

# #브로드 캐스팅
# lst = list(range(6))
# lst

# lst[3]=-1
# lst

# arr1d = np.arange(8)
# arr1d

# arr1d[3:6]=100
# arr1d

# #view
# arr2d =np.arange(20).reshape(4,-1)
# arr2d

# arr2d[0]

# arr2d[1][2] #재귀적 접근/1행 2열


# arr2d[1,2]

# arr2d[:3][:2]  #,가 없으면 행과 행으로 표현

# arr2d[:3,:2]


# arr = np.array([0,1,2,3,4])
# arr[[True,False,True,False,True]]


# arr2d =np.arange(20).reshape(4,5)
# arr2d


# arr2d[[0,2]] #0행과 2행 #multi index는 []더 추가해야 함.

# arr2d[[0,3], [4]]

# #유니버설 함수
# arr = np.arange(-3,3).reshape(3,-1)
# arr

# np.exp(arr)

# #floor: 소수점 버리기
# np.floor(arr)

# #이항 유니버설 함수
# arr1= np.arange(8).reshape(2,-1)
# arr2=np.arange(-40,40,10).reshape(2,-1)
# print(arr1)
# print(arr2)


# np.maximum(arr1,arr2)

# np.subtract(arr1,arr2)


# np.multiply(arr1,arr2)

# arr= np.arange(4).reshape(2,2)
# arr

# arr.sum()

# arr.sum(axis=0) #열 합계

# arr.sum(axis=1) #행 합계

# arr.mean(axis=0) #열 평균 소수점

# arr.mean(axis=1) #행 평균


# #where
# # x if 조건 else y의 벡터화 버전
# xarr = np.array([100,200,300,400])
# yarr = np.array([1,2,3,4])
# cond = np.array([True,False,True,False])


# result =np.where(cond,xarr,yarr)
# result

# np.where(xarr>200, max(xarr),0)

# np.where(xarr%3==0,1,0)

# #sort()
# np.random.seed(42)
# arr = np.random.randint(1,100, size=10) #1~100 정수중에 10개 뽑아주세요
# arr

# arr.sort()
# arr

# -np.sort(-arr) #부호를 이용하여 내림차순으로 정렬, array의 sort에서는 내림차순, 오름차순 선택 옵션이 없다

# lst =[1,32,4,1,20]
# lst.sort(reverse=True)  #내림차순으로 정렬
# lst

# import numpy as np
# identity =np.eye(4)
# print(identity)

# identity =np.eye(2,3)
# print(identity)

# x = np.arange(9).reshape(3,-1)
# print(x)

# np.diag(x)

# a = np.arange(4).reshape(-1,2)
# print(a)

# a*a

# np.multiply(a,a)

# np.dot(a,a)

# a.dot(a)

# #matmul:matrix multiplication
# a= np.random.randint(-3,3, 10).reshape(2,5)
# b= np.random.randint(0, 5, 15).reshape(5,3)
# b

# #
# #

# ab = np.matmul(a,b)
# print(ab.shape,'\n') #\n 개행
# print(ab)

# # ba =np.matmul(b,a) 실행안됨
# # ab=np.matmul(a,b.T) 실행안됨


# np.dot(a,b) #dot -> 1차원 벡터 공식문서에는 2D(2차원) matmul로 돌아감



# import numpy as np
# import pandas as pd


# obj = pd.Series([0,1,2,3,4,5,6,7], index=['a','b','c','d','e','f','g','h'], dtype='int64')
# obj

# #integer location based
# obj[3]

# obj[-1]

# obj[[1,3,5]]

# obj[1:3]

# obj<3

# obj[obj<3]



# label location based


# obj

# obj.g

# obj['c']

# obj[['e','c']]

# obj['a':'c']

# obj['d':'e']

# obj['d':'e']=100
# obj

# obj = pd.Series([0,1,2,3,4,5,6,7], index=['a','b','c','d','e','f','g','h'], dtype='int64')
# obj
# obj.iloc[2]

# obj.iloc[[2]]

# obj.iloc[1:4]

# obj.loc['a':"c"]

# df =pd.DataFrame(np.arange(24).reshape(4,-1), columns=['c1','c2','c3','c4','c5','c6'], index=['r1','r2','r3','r4'])
# df

# df.c3

# df[['c1','c3']]

# df['r1':"r2"]

# df['c1':'c2'] #열 중심이라서 결과값을 반환못함

# df[['c1','c2']]

# iloc


# df.iloc[[0],[3]]

# df.iloc[[0,1],1:4]

# - loc


# df.loc[['r1'],['c4']]

# df.loc['r1':'r2', ['c3','c4','c2']]

# - 산술 연산자

# s1 = pd.Series([1,2,3,4], index=['a','b','c','d'])
# s2 = pd.Series([10,20,30,40], index=['a','b','c','d'])
# s1+s2

# s1 = pd.Series([1,2,3,4], index=['a','b','c','d'])
# s2 = pd.Series([10,20,30,40], index=['b','c','d','e'])
# s1+s2  #SQL의 Outer join

# s1.add(s2,fill_value=0)

# s2.add(s1,fill_value=0)

# import pandas as pd
# stock = pd.read_csv('https://raw.githubusercontent.com/Youngpyoryu/Lecture_Note/main/%ED%8C%8C%EC%9D%B4%EC%8D%AC/stock_2020_01.csv', encoding='CP949')
# stock

# stock = pd.read_csv('/content/stock_2020_01.csv', encoding='CP949')
# stock

# stock.head() #위에서 5개

# stock.tail() #아래에서 5개

# - 기술통계량

# stock.describe() #중앙값 median =50%, 중앙값=평균일때 정규분포 (대칭)

# A =np.array([1,2,4,8,10])
# np.mean(A)


# A =np.array([1,2,4,8,10])
# np.median(A) #중위값 중간값

# - 결측치(missing value)

# # stock.isna().sum()
# stock.isna()


# stock.info()

# stock['Date']

# stock['kospi'].sort_values()

# - unique
#   - 중복되는 값을 제거하고 유일한 값만 담고 있는 Series를 반환

# obj = pd.Series([2,1,3,3,1,5,np.nan,1,2])
# obj

# obj.isnull().sum()

# obj.unique() #unique는 Series밖에 안 됨, dataframe에서는 사용 불가


# stock['kospi'].unique()

# - 정렬
#   - value_counts

# obj.value_counts()

# obj.sort_values()

# obj.value_counts(normalize=True) #0~1사이값 만드는 과정

# obj = pd.Series([1,2,3,-1,-2], index=list('adebc'))
# obj

# obj.sort_index(ascending=False)

# obj = pd.Series([1,2,3,-1,-2], index=list('가마나라다'))
# obj

# frame = pd.DataFrame(np.arange(9).reshape(3,3), index = list('abc'), columns= list('edf'))
# frame

# frame.sort_index()

# frame.sort_index(axis=1) #1이 열로 인식한다

# frame.sort_values(by='e',ascending=False)

# frame.sort_values(by=['e','f'],ascending=False)

# series = pd.Series([100, 200, 300])
# series

# series.map({100:'C',200:'B',300:'A'})


# series.map('${}'.format)

# series.map('{}달러'.format)



# f =lambda x: np.add(x,3)
# series.map(f)

# - apply함수
#   - map보다 적용할 수 있는 범위가 큰 것

# s = pd.Series([20,21,12], index=['London','New York', 'Helsinki'])
# s

# def sub_custom_value(x,val):
#   return x-val

# s.apply(sub_custom_value,args=(10,)) #10, 이유는 iterable 순환하게 하기 위해. 만일 값이 10이면 에러

# def add_custom_values(x,**kwargs):
#   for month in kwargs:
#     x +=kwargs[month]
#   return x
  

# s.apply(add_custom_values, june=30, july=20, august=25)

