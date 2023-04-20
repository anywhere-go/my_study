# egg_list = ["달걀1","달걀2","달걀3"]
# for egg in egg_list:
#     print(egg + ": 달걀 프라이를 만듭니다.")


# 0: 달걀 프라이를 만듭니다 ~ 99: 달걀 프라이를 만듭니다
# egg_list = range(100)
# for egg in egg_list:
#     print(str(egg)+": 달걀 프라이를 만듭니다.")


#3! 6! 9!출력
count = range(10)
for n in count:
    if (n + 1) % 3 != 0:
        continue
    print(str(n +1) + "!")