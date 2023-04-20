# age = 19
# money = 26000
# chicken = 20000
# beer = 10000
# drink = 5000
# if money >= chicken:
#     print("치킨을 시켜 먹는다.") 
#     money = money - chicken   
# if money >=beer and age >=20:
#     print("맥주를 마신다")
#     money = money - beer
# if money >= drink:
#     print("음료수를 시켜 먹는다.")
#     money = money - drink

age = 19
money = 25000
chicken = 20000
beer = 10000
drink = 5000
if money >= chicken + beer + drink and age >= 20:
    print("치킨, 맥주, 음료수 다 시켜 먹는다.")
elif money >= chicken + beer and age >= 20:
    print("치맥 먹는다.") 
elif money >= chicken:
    print("치킨 먹는다")
elif money >= drink + chicken:
    print("음료수와 치킨을 시켜 먹는다.")





# if money >= chicken:
#     print("치킨을 먹는다.")
#     if money - chicken >= beer and age >=20:
#         print("맥주를 먹는다")
#         if money -chicken -beer >= drink:
#             print("음료수를 먹는다")
# elif money >= beer and age >=20:
#     print("맥주를 먹는다.")
#     if money - beer >= drink:
#         print("음료수를 먹는다.")
# elif money >= drink:
#     print("음료수를 먹는다")