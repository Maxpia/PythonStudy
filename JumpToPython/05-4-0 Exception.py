# Exception.py
class MyError(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg

def say_nick(nick):
    if nick == "바보":
        raise MyError("%s는 허용되지 않음" % nick)
    else:
        print(nick)

try:
    say_nick("천사")
    say_nick("바보")
except MyError as e:
    print(e)
finally:
    print("끝!")