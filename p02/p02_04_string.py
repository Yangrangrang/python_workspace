'''
문자열
API: https://docs.python.org/ko/3/library/functions.html
'''


def main():
    str01 = "Life is too short, You need Python"
    print("str01:{}, type:{}".format(str01, type(str01)))

    str02 = '123'
    print('str02:{}, type:{}'.format(str02, type(str02)))

    str02 ="Hello" + " " + "World"
    print("str02:{}, type:{}".format(str02, type(str02)))

    print("--"*50)
    print("--")
    print("--"*50)

    # 문자열에 작은따옴표(') 포함 시키기
    food = "Python's favorite food is perl"
    print("food:{}".format(food))   # food:Python's favorite food is perl

    # unterminated string literal (detected at line 25)
    # food = 'Python's favorite food is perl'   #ERR

    # 문자열에 큰 따옴표(") 포함 시키기
    food = '"Python favorite" food is perl'
    print("food:{}".format(food))

    # 백슬러시(\)를 사용해서 작은따옴표(')와 큰따옴표(")를 문자열에 포함시키기
    food = 'Python\'s favorite food is perl'
    print("food:{}".format(food))

    print("=="*30)

main()
