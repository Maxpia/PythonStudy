#coffee.py

coffee = 10
while True:
    money = int(input("돈을 넣어 주세요: "))
    if money == 300:
        print("커피를 줍니다.")
        coffee = coffee - 1
    elif money > 300:
        print("거스름돈 %d과 커피를 줍니다." % (money - 300))
        coffee = coffee - 1
    else:
        print("돈이 모자랍니다.")
        print("남은 커피는 %d잔 입니다." % coffee)
    
    if not coffee:
        print("커피가 다 떨어졌습니다. 판매 중지 합니다.")
        break
