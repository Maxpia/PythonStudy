# 상속 클래스 연산.py
class House:
    def travel(self, where):
        print("%s가 %s여행 감." % (self.fullname, where))
    
    def __add__(self, other):
        print("%s와 %s가 결혼함." % (self.fullname, other.fullname))
    
    def __sub__(self, other):
        print("%s가 %s를 사별함." % (self.fullname, other.fullname))
    
    def __mul__(self, other):
        return ("%s와 %s에게 아이가 생김." % (self.fullname, other.fullname))
    
    def __truediv__(self, other):
        return ("%s와 %s가 이별함." % (self.fullname, other.fullname))

class HousePark(House):
    lastname = "박"
    def __init__(self, name):
        self.fullname = self.lastname + name

class HouseKim(HousePark):
    lastname = "김"
    def travel(self, where):
        print("%s가 %s여행 가고 싶어함." % (self.fullname, where))

park = HousePark("진영")
kim = HouseKim("민수")
park.travel("부산")
kim.travel("서울")
print(park + kim)
print(park - kim)
print(park * kim)
print(park / kim)
