# 예외 처리(오류처리라고 할 수 있다)
# 오류 발생을 잡아내서 처리하는 것
li = [1,2,3,4,5]
li[100]

100/0

f = open("없는파일", "r")

#에러 발생 시 프로그램을 중단하고 에러메시지를 보여준다.
#try ~ except
#try 블록에는 오류가 발생할 수 있는 코드
#except 블록에는 오류가 발생했을 때 수행할 코드
try:
    100 / 0
except ZeroDivisionError as e:
    print(e)

print("에러 발생 후")

# try:
#     100 / 0
# except:
#     print("에러 발생")

# print("에러 발생 후")


#에러 없을 때 except 블록 실행이 되지 않는다
# try:
#     100 / 10
# except:
#     print("에러 발생")

# print("에러 발생 후")

#에러 메시지 출력
# try:
#     100 / 0
# except Exception as e: #에러 메시지(오류 메시지)를 e라고 한다
#     print(e)

# print("에러 발생 후")

#
# try:
#     [1,2,3,4,5][100] #index 범위 초과 오류
# except ZeroDivisionError as e: #0으로만 나온 것만 잡는 예외처리
#     print(e, "0으로 나눌 수 없습니다.")

# print("에러 발생 후")

#
# try:
#     [1,2,3,4,5][100] #index 범위 초과 오류
# except ZeroDivisionError as e: #0으로만 나온 것만 잡는 예외처리
#     print(e, "0으로 나눌 수 없습니다.")
# except IndexError as e:
#     print(e, "인텍싱할 수 없습니다.")

# print("에러 발생 후")

# finally 
# 예외 발생 여부와 상관 없이 항상 수행되는 코드

try:
    f = open("없는 파일", "r")
except:
    print("에러 발생")
finally:
    f.close()

# else
# 오류가 발생하지 않으면 실행되는 코드
try:
     age = int(input("나이: "))
except:
    print("입력이 잘못되었습니다.")
    print("숫자를 입력해주세요.")

else: 
    if age >= 20:
        print("성인입니다")
    else:
        print("미성년자입니다")

class Bird:
    def fly(self):
        raise NotImplementedError   #구현되지 않은 에러 출력
    
my_bird = Bird()
my_bird.fly()

# 4월 26일 마지막 시간 문제
# max_limit_calculator.py 파일에 작성하세요
# my_calculator 모듈의 MyCalculator클래스를 상속받아서 MaxLimitCalculator 클래스를 정의하세요
# add, sub, mul, div 메소드를 사용하여 더하기, 빼기, 곱하기, 나누기를 할 수 있다.
# 0으로 나눴을 때 에러가 발생하지 않도록 처리한다.
# 입력되는 정수가 1개라도 100보다 크면 계산하지 않고, 100이하의 값을 입력하도록 안내 메시지를 출력한다
# 계산 결과가 100보다 크면 계산하지 않고 100이하의 결과가 나오는 값을 입력하도록 안내 메시지를 출력한다
