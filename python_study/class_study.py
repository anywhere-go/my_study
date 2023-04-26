# 객체지향 (oop, objict oriented programming)
# c,c++, java 등
# 객체와 객체 사이의 상호작용으로 프로그램을 구성하는 프로그래밍 패러다임

# 객체지향의 특징 4가지
# 추상화: 공통된 속성이나 기능 도출 (주요한 특징을 남기는 작업--나중에 재사용 위함)
# 캡슐화: 데이터의 구조와 연산을 결합 (한바구니에 담는다)
# 상속 : 상위 개념의 특징이 하위 개념에 전달 (자동차 예시- 트럭)
# 다형성 : 유사 객체의 사용성을 그대로 유지

# 객체는 추상화와 캡슐화의 결과라고 생각하면 편하다
# 객체는 데이터 필드와 메소드를 가진다.


# 클래스는 객체를 정의한 것 (객체의 설계도)
# 데이터 필드(멤버 변수, 속성 attribute)- 객체가 가지고 있는 변수 의미
# 메소드 (멤버 함수)- 객체가 가지고 있는 함수 의미한다

"""
class 클래스이름:
    클래스 멤버 변수
    메소드
"""

# 클래스 이름도 변수 이름 규칙 지켜야 함
# 클래스 이름 컨벤션(관용)
# 첫 글자 대문자
# 언더바(_) 안쓰기
# 단어 구분될 때 대문자

# 자동차 class 예시
# class Car: #첫글자 대문자
#     pass

# class SportsCar: #단어구분 첫글자 대문자
#     pass

# class Car: #첫글자 대문자
#     def move(self): #메소드 
#             print("move")

# class SportsCar: #단어구분 첫글자 대문자
#     pass

# my_car = Car() #인스턴스 (사례, 경우, 집합 안의 개별요소)
# my_car.move()  #my_car 객체를 통해서(.) move해줘!!

# 인스턴스 (위에서 my_car가 Car class의 인스턴스)
# 클래스를 통해 생성된 객체
# .  -----> (my_car.move()) 점은 객체 멤버 접근 연산자 의미한다, list도 객체이어서 .(점)붙여서 접근했다

# li = [1,2,3,4,5]
# li.append(6)
# print(li)
# 파이썬에서는 모든 게 객체다 (int, float, tuple, str, list 등)
# 내장함수 type()
# 데이터의 자료형을 반환한다
# print(type(li))

# n = 10
# print(type(n))
# print(type("Hello"))


# str(문자열) 메소드
# upper()
# 모두 대문자로 변경
# s= "Hello"
# s.upper()
# print(s.upper())

# lower()
# 모두 소문자로 변경
# s= "Hello"

# print(s.lower())

# strip()
# 문자열 양쪽 끝의 특정 문자를 제거
# s1= "    Hello    "
# print(s1.strip())

# lstrip(), rstrip()
# 왼쪽, 오른쪽 끝의 특정 문자 제거

# print(s1.lstrip())
# print(s1.rstrip())

# split()
# 문자열에서 구분자로 분할하여 리스트로 반환
# s2 = "Hello,World,Python"
# print(s2.split(','))

# replace()
# 문자열의 특정 부분을 다른 것으로 대체한다
# print(s2.replace(',',' '))

# s1, s2 등은 string객체이며, immutable(수정 불가)이다
# 그래서 같은 변수 이름을 쓰고 싶으면 재활당(객체 값을 수정함)
# s2 = s2.replace(',', ' ')
# print(s2)

# "Hello" --> "hello" 변경할려면 재활당 2가지 방법 (같은변수.lower , 변수 =같은변수.replace("대상","수정")
# s3 = "Hello"
# s3.lower()
# s4 = s3.replace("H", "h")
# print(s3)
# print(s4)

# self 매개변수(파라미터)
# 모든 메소드의 첫번째 매개변수 (필수적으로 들어간다)
# 메소드의 정의에는 사용되지만, 호출에는 사용되지 않음
# 객체 자신을 참조하여 클래스에 정의된 멤버에 접근할 때 사용
# class Person:
#     def say(self):
#         print("Hello")
#     def move(self):
#         pass
#     def eat(self, food):
#         print(f"{food} 먹었습니다.")
#     def sleep(self):
#         pass

# person1 = Person()
# person1.say()  #함수 호출할 때 self 안 씀
# person1.eat("밥") #호출할 때 self안쓰고 food만 넣는다


# class Person:
#     def say(self):
#         self.name ="사람1"
#         print("Hello")
#     def move(self):
#         pass
#     def eat(self, food):
#         self.sleep
#         print(f"{self.name}이{food} 먹었습니다.")
#     def sleep(self):
#         print(f"{self.name}이 잠을 잤습니다.")

# person1 = Person()
# person1.say()  #함수 호출할 때 self 안 씀
# person1.eat("밥") #호출할 때 self안쓰고 food만 넣는다
# person1.sleep()


# initializer 초기자
# initialize 초기화 (값을 가지게 만든다)

# class Person:
#     def __init__(self):
#         print("initialize")

# print('before')
# person2 = Person("이름", 20, "성별", "010-1234-5678")  # 이때 print("initialize")실행 된다
# print('after')

# 새롭게
# class Person:
#     def __init__(self, name, age, gender, phone):# 초기 항상 self가 먼저 오고 다른 객체가 온다
#         self.name = name  # 매개변수(self.name)에 name 넣는다
#         self.age = age
#         self.gender = gender
#         self.phone = phone
#         print("initialize")
    
#     def say_name(self):
#         print(self.name)
# # Person 클래스에 introduce 메소드를 추가
# # 이름, 나이, 성별을 print하는 메소드
#     def introduce(self):
#         print(f"안녕하세요. 저는 {self.name}입니다.")
#         print(f"나이는 {self.age}살이고, 성별은 {self.gender}입니다.")

#         print(self.name, self.age, self.gender, self.phone)

# print('before')
# person2 = Person("최강", 20, "남자", "010-1234-5678")  # 이때 print("initialize")실행 된다
# print('after')
# person2.say_name()
# person2.introduce()
# print(person2.phone)

# 상속 inheritance
# 상위 클래스 상속받아 하위 클래스에 영향을 준다

class Animal:
    def __init__(self, name):
        self.name = name  #name값을 멤버변수로 저장한다. 서로 다른 객체이다(값이 똑같은 다른 객체이다)
        print(f"{self.name}가 생성되었습니다.")

    def say(self):
        print("")

class Dog(Animal): #Dog가 Animal 상속받음
    # 메소드 재정의
    # method overriding
    def say(self):
        print("멍멍")

my_dog = Dog("백구")
my_dog.say()

class Cat(Animal):
    def say(self):
        print("야옹")

my_cat = Cat("나비")
my_cat.say()
        

class Student:
    def __init__(self, name, age, school, grade):
        #이름, 나이, 학교, 학년을 멤버 변수로 저장하는 메소드를 정의하세요.
        self.name = name
        self.age = age
        self.school = school
        self.grade = grade

    def introduce(self):
        #이름, 나이, 학교, 학년을 print하는 메소드를 정의하세요
        print(f"{self.name},{self.age},{self.school},{self.grade}")
        print(f"안녕하세요 저는 {self.name}이고, 나이는 {self.age}살입니다.")
        print(f"그리고 학교는 {self.school}이고, {self.grade}학년입니다.")


stu1 = Student("홍길동", 20, "서울대학교", 1)
stu2 = Student("손흥민", 21, "서울대학교", 2)
stu3 = Student("류현진", 22, "서울대학교", 3)

stu_list = [stu1, stu2, stu3]
for stu in stu_list:
    stu.introduce()
