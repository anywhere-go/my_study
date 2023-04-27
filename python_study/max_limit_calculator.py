# 4월 26일 마지막 시간 문제
# max_limit_calculator.py 파일에 작성하세요
# my_calculator 모듈의 MyCalculator클래스를 상속받아서 MaxLimitCalculator 클래스를 정의하세요
# add, sub, mul, div 메소드를 사용하여 더하기, 빼기, 곱하기, 나누기를 할 수 있다.
# 0으로 나눴을 때 에러가 발생하지 않도록 처리한다.
# 입력되는 정수가 1개라도 100보다 크면 계산하지 않고, 100이하의 값을 입력하도록 안내 메시지를 출력한다
# 계산 결과가 100보다 크면 계산하지 않고 100이하의 결과가 나오는 값을 입력하도록 안내 메시지를 출력한다

# 강사 20230427 1교시
from my_calculator import MyCalculator
class MaxLimitCalculator(MyCalculator):
    def add(self, n1, n2): #메소드 재정의(덮어쓰기 하는 것)
        if n1 > 100:
            print("100보다 작은 수를 입력하세요.")
        elif n2 > 100:   
            print("100보다 작은 수를 입력하세요.")
        else:
            result = n1 + n2
            if result > 100:
                print("계산결과가 100보다 작은 수를 입력하세요.")
            else:
                print(f"{n1}+ {n2} = {n1 +n2}")

    def sub(self, n1, n2):
        if n1 > 100:
            print("100보다 작은 수를 입력하세요.")
        elif n2 > 100:   
            print("100보다 작은 수를 입력하세요.")
        else:
            result = n1 - n2
            if result > 100:
                print("계산결과가 100보다 작은 수를 입력하세요.")
            else:
                print(f"{n1}- {n2} = {n1 -n2}")
        
    def mul(self, n1, n2):
        if n1 > 100:
            print("100보다 작은 수를 입력하세요.")
        elif n2 > 100:   
            print("100보다 작은 수를 입력하세요.")
        else:
            result = n1 * n2
            if result > 100:
                print("계산결과가 100보다 작은 수를 입력하세요.")
            else:
                print(f"{n1}* {n2} = {n1 *n2}")

    def div(self, n1, n2):
        if n1 > 100:
            print("100보다 작은 수를 입력하세요.")
        elif n2 > 100:   
            print("100보다 작은 수를 입력하세요.")
        # elif n2 == 0: #다른 것보다 조건이 하나더 추가 
        #     print("0으로 나눌 수 없습니다")
        else:
            try:
                result = n1 / n2
            except ZeroDivisionError:
                print("0으로 나누지 마세요")
            result = n1 / n2
            if result > 100:
                print("계산결과가 100보다 작은 수를 입력하세요.")
            else:
                print(f"{n1} / {n2} = {n1 / n2}")

my_max_limit_calculator = MaxLimitCalculator()  # 값을 초기상태로 객체 만들고 변수에 저장
my_max_limit_calculator.div(100, 0)



