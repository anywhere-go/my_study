def add(a, b):
    return a + b

def sub(a, b):
    return a - b
if __name__ =="__main__":  #다른 프로그램에서 import할때 name이 메인이 아닌 모듈이름이 됨
    print(add(1,2))
    print(sub(3,4))
else:
    print(__name__) #false일때 모듈이름 출력하라
