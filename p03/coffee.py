#coffee.py

coffee = 10
money = 300

while money:
    print("돈을 받았으니 커피를 줍니다")

    coffee = coffee - 1

    print("남은커피는 %d잔 입니다." % coffee)

    if coffee == 0:
        print("커피가 다 떨어졌습니다.")
        break

'''
돈을 받았으니 커피를 줍니다
남은커피는 9잔 입니다.
돈을 받았으니 커피를 줍니다
남은커피는 8잔 입니다.
돈을 받았으니 커피를 줍니다
남은커피는 7잔 입니다.
돈을 받았으니 커피를 줍니다
남은커피는 6잔 입니다.
돈을 받았으니 커피를 줍니다
남은커피는 5잔 입니다.
돈을 받았으니 커피를 줍니다
남은커피는 4잔 입니다.
돈을 받았으니 커피를 줍니다
남은커피는 3잔 입니다.
돈을 받았으니 커피를 줍니다
남은커피는 2잔 입니다.
돈을 받았으니 커피를 줍니다
남은커피는 1잔 입니다.
돈을 받았으니 커피를 줍니다
남은커피는 0잔 입니다.
커피가 다 떨어졌습니다.
'''
    
