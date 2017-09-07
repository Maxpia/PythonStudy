# Class.py
class Service:
    secret = "영구는 외계인"
    
    def setname(self, name):
        self.name = name
    
    def sum(self, a, b):
        result = a + b
        print("%s님 %d + %d = %d입니다." % (self.name, a, b, result))

pay = Service()     # pay는 객체입니다. 그리고, pay는 Service 클래스의 인스턴스 입니다.
pay.setname("홍길동")  # setname는 Service 클래스의 매소드 입니다.
pay.sum(1, 1)

kim = Service()
kim.name = "김병일"    # 입력 하지 않으면 오류
kim.sum(1, 1)


class Service_Init:
    secret = "영구는 외계인"  #클래스 변수(클리스의 인스턴스에서 공통으로 같은 값이 유지 된다.)
    
    def __init__(self, name = ""):
        if name == "":
            self.name = input("이름을 입력해 주세요. : ")
        else:
            self.name = name
    
    def sum(self, a, b):
        result = a + b
        print("%s님 %d + %d = %d입니다." % (self.name, a, b, result))
        
pay = Service_Init("홍길동")
pay.sum(1, 1)

kim = Service_Init()
kim.sum(1, 1)