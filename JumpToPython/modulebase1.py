# 모듈.py
def sum(a, b):
    return a + b
    
def safe_sum(a, b):
    if type(a) != type(b):
        return "더할수 있는 것이 아닙니다."
    else:
        result = sum(a, b)
        return result

print (__name__)

if __name__ == "__main__":  # import 에서는 실행되지 않음.
    print(safe_sum('a', 1))
    print(safe_sum(1, 4))
    print(sum(10, 10.4))