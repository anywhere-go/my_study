# tuple(튜플)형
# 튜플은 element의 값이 정해지면 값을 수정할 수 없다!!
# mutable(변화할 수 있는, 값 수정가능) / immutable(불변하는)
# mutable에는 list, dict이 해당
# immutable 수정 불가능
# immutable에는 int, float, str, tuple 등이 속한다
# my_list =[1,2,3]
# my_list[0] = 5
# print(my_list)

# my_tuple = (1,2,3)
# my_tuple[0] = 5 #Error 튜플형은 수정 불가능하기 때문, 삭제도 불가능
# print(my_tuple)

# tuple_1 =("Hello","World","python")
# t2 = (1,2,3,4,5)
# t3 = (1,2, "Hello")
# t4 = 1,2,3
# t5 = (1,2,(3,4,5))

# t6 = tuple_1 + t2
# t7 = t3 * 3
# t7 = t3 * 4
# print(t7)

# t3 = (1,2, "Hello")
# print(t3[2])
# print(t3[0:2])
# print(len(t3))

# t5 = (1,2,(3,4,5))
# print(t5[2][1])

# t8 = (5, 3, 1, 4, 2)
# for i in t8:
#     print(i)
