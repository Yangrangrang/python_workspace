'''
객체의 고유한 값(id)인 주소를 식별할 수 있다.
'''


def main():
    a = 500
    print(id(a))    # 4337412400

    b = a
    print(id(b))    # 4337412400

    print("-"*35)
    c = [1, 2, 3]
    d = [1, 2, 3]
    print('c:{}'.format(id(c)))
    print('d:{}'.format(id(d)))

    c = d
    print('c:{}'.format(id(c)))
    print('d:{}'.format(id(d)))

    print('c is d:{}'.format(c is d))   # c is d:True

    d[0] = 99
    print('d:{}'.format(d))
    print('c:{}'.format(c))

main()
'''
c:4334557760
d:4334626496
c:4334626496
d:4334626496
c is d:True
d:[99, 2, 3]
c:[99, 2, 3]
'''