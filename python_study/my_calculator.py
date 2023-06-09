#계산기 만들기
#기능:
#add(), sub(), mul(), div() 함수 정의
#input() 함수 활용
#정수 2개, 사칙연산 선택을 입력받은 후
#계산 결과를 print한다.
#계산식과 결과를 calculator_result.txt파일에 저장 기록한다
#사용자가 'q'를 입력하면 종료한다


#함수 정의하기 전 에러 발생
# while True:
#     print("""
#     계산기
#     1: +
#     2: -
#     3: *
#     4: /
#     q: 종료
#     """)
#     operator = input('원하는 계산을 입력하세요')
#     if  operator == 'q':
#         break
#     a = int(input('정수 1:'))
#     b = int(input('정수 2:'))

#     if operator == '1':
#         add(a, b)
#     elif operator =='2':
#         sub(a, b)
#     elif operator =='3':
#         mul(a, b)
#     elif operator =='4':
#         div(a, b)

#     with open("python_study/calculator_result.txt", 'a',encoding="utf-8") as f:
#          f.write(str(result))

# add_write(1, 2)


#함수정의하고 계산

# def add(a, b):
#     result = str(a) +"+"+str(b)+"="+str(a+b) # result ="%d + %d = %d" % (a, b, a+b)
#     print(result)
#     with open("python_study/calculator_result.txt", 'a', encoding='utf-8') as f:
#         f.write(result)
# def sub(a, b):
#     result = str(a) +"-"+str(b)+"="+str(a-b)
#     print(result)
#     with open("python_study/calculator_result.txt", 'a', encoding='utf-8') as f:
#         f.write(result)
# def mul(a, b):
#     result = str(a) +"*"+str(b)+"="+str(a*b)
#     print(result)
#     with open("python_study/calculator_result.txt", 'a', encoding='utf-8') as f:
#         f.write(result)
# def div(a, b):
#     result = str(a) +"/"+str(b)+"="+str(a/b)
#     print(result)
#     with open("python_study/calculator_result.txt", 'a', encoding='utf-8') as f:
#         f.write(result)

# while True:
#     print("""
#     계산기
#     1: +
#     2: -
#     3: *
#     4: /
#     q: 종료
#     """)
#     operator = input('원하는 계산을 입력하세요')
#     if  operator == 'q':
#         break
#     a = int(input('정수 1:'))
#     b = int(input('정수 2:'))

#     if operator == '1':
#         add(a, b)
#     elif operator =='2':
#         sub(a, b)
#     elif operator =='3':
#         mul(a, b)
#     elif operator =='4':
#         div(a, b)

# 문자열 포맷팅 해보기

# MyCalculator 클래스로 만들기
# add, sub, mul, div 메소드
class MyCalculator:
    def __init__(self):
        pass

    def add(self, ni, n2):
        print(f"{n1}+{n2} = {n1+n2}")
    def sub(self, ni, n2):
        print(f"{n1}-{n2} = {n1-n2}")
    def mul(self, ni, n2):
        print(f"{n1}*{n2} = {n1*n2}")
    def div(self, ni, n2):
        print(f"{n1}/{n2} = {n1/n2}")

    # def sub(self, n1, n2:):
    
if __name__ == "__main__":
    my_calculator = MyCalculator()
    while True:
        print("""
            계산기
             1: +     
             2: -
             3: *
             4: /
             q: 종료
             """)
        operator = input()
        if operator == 'q':
            print("종료합니다")
            break
        n1 = int(input())
        n2 = int(input())
        if operator == "1":
            my_calculator.add(n1, n2)
        elif operator == "2":
            my_calculator.sub(n1, n2)
        elif operator == "3":
            my_calculator.mul(n1, n2)
        elif operator == "4":
            my_calculator.div(n1, n2)
        else:
            print("입력을 잘못했습니다")
