#dictionary 딕셔너리 자료형 {중괄호 사용}
# key-value 형태
# key: value
# {"이름":"이름", "나이": 18, "점수": 80}
# {"이름":"이름", "나이": 18, "점수": [80, 90, 100]}
# {"이름":"이름", "나이": 18, "점수": [80, 90, 100], 1:"ㅎㅎ"}

# person={
#     "이름":"이름", 
#     "나이": 18, 
#     "점수": {
#         "영어":80,
#         "국어":90,
#         "수학":100
#     },
#     1:"ㅎㅎ"
# }
# print(person["나이"])
# print(person["점수"]["영어"])

person={
    "이름":"이름", 
    "나이": 18, 
    "점수": {
        "영어":80,
        "국어":90,
        "수학":100
    },
    1:"ㅎㅎ"
}
print(person["나이"])
print(person["점수"]["영어"])

# dict_1 = {1:'a'}
# dict_1['b']=2 #'b':2 key-value 쌍 추가
# dict_1[1] ='c'
# del dict_1[1]
# print(dict_1)
dict_2 = {1:'a', 2:'b', 3:'c'}
#keys()
#딕셔너리에서 key 값만 리스트 형태로 돌려준다
dict_keys =(dict_2.keys())
print(dict_keys)
#values()
dict_values =dict_2.values()
print(dict_values)

#items()
#딕셔너리에서 key-value 쌍을 듀플로 묶은 값을 리스트 형태로 돌려준다
dict_items = dict_2.items()
print(dict_items)

#get()
# dict_2.get["나이"]
# dict_2["나이"]
# print(dict_2.get("나이"))
print(dict_2.get("나이", "나이 불명"))


#clear()
dict_2.clear()
print(dict_2)