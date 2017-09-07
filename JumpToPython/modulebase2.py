# modulebase2.py
PI = 3.141592

class Math:
    def solv(self, r):
        return PI * (r ** 2)
        
def sum(a, b):
    return a + b
 
if __name__ == "__main__":  # import 에서는 실행되지 않음.
    print(PI)
    a = Math()
    print(a.solv(2))
    print(sum(PI, 4.4))
    dir(a)