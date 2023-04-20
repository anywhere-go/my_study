# li_1 = ["Hello","World","Python"]
# #Hello World Python이라고 출력하세요
# print(li_1[0], li_1[1], li_1[2])
#join(리스트)
# 리스트의 문자열을 합친다.
#"/".join(li_1)
# "*".join(li_1)
# print(" ".join(li_1))
# print(li_1[0] + "" +li_1[1] +"" + li_1[2]) #HelloWorldPython
# #li_1의 원소를 사용하여
# #Help라고 출력하세요
# print(li_1[0][0:3]+li_1[2][0])
# print(li_1)
# li_2 = [1, 2, 3]
# # li_1과 li_2를 사용하여
# #["Hello". "World", "Python", 1, 2, 3]출력
# print(li_1 + li_2)

# li_1.entends(li_2)
# #li_1과 li_2를 사용하여
# #["Hello", 1, "World",2, "Python",3]를 출력
# li_1.insert(1, li_2[0])
# li_1.insert(3, li_2[1])
# li_1.insert(5, li_2[2])
# print(li_1)

# li_1 =["Hello","World","Python"]
# li_1.insert(1, li_2[0])
# li_1.insert(3, li_2[1])
# li_1.append(li_2[2])
# print(li_1)

# # print([i[0, i[1] for i in zip()]])



# scores = []
# scores = list()

# scores.append(int(input("영어 점수:")))
# scores.append(int(input("국어 점수:")))
# scores.append(int(input("수학 점수:")))

# avg = (scores[0] +scores[1] + scores[2])/3
# avg = sum(scores) / 3
# #sum()
# #리스트 요소를 모두 더한다, 단 숫자만 합친다
# if avg >= 91:
#     print("A학점 축하드립니다!")
# elif avg >=81:
#     print("B학점 입니다!")
# elif avg >=71:
#     print('C학점 입니다!')
# elif avg >=61:
#     print("D학점 입니다!")
# else :
#     print("안타깝지만 F학점 입니다!")


#나이와 가지고 있는 돈을 입력받는다
#가지고 있는 돈으로 물건을 몇 개 살 수 있는지와 잔돈 출력
#물건의 가격은 500원이다.
#
#나이와 가지고 있는 돈을 입력
#가지고 있는 돈으로 물건별로 각각
#몇 개 살 수 있는지와 잔돈을 출력
#물건의 가격은 1번 물건 1000원
#2번 물건 50원 3번 물건 120원이다.

# age = []
# age.append(int(input("나이:")))
# myMoney = int(input('가진 돈:'))

# price = int(input('물건값:'))

# item_cnt = myMoney / price
# change = myMoney - (item_cnt*price)
# print('물건 갯수: %d'%item_cnt)
# print('잔돈: %d'%change)

# age = []
# age.append(int(input("나이:")))
# myMoney = int(input('가진 돈:'))

# price1 = int(input('물건값1'))
# price2 = int(input('물건값2'))
# price3 = int(input('물건값3'))
# sum(price)
# item_cnt = myMoney / (item_cnt*price)
# change = myMoney - price
# print('물건 갯수: %d'%item_cnt)
# print('거스름돈: %d'%change)



# age = input("나이:")
# money = int(input("돈:"))
# price = 500
# print(money // price)
# print(money % price)


# age = input("나이:")
# money = int(input("돈:"))
# prices = [1000, 50, 120]
# print(money // prices[0], money % prices[0])
# print(money // prices[1], money % prices[1])
# print(money // prices[2], money % prices[2])
