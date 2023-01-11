'''

'''


def main():
    d = {'a':123321, 'kim':'pacmk', 'b':'blog', 'c':333,123:'name'}

    # items() 출력
    # dict_items([('a', 123321), ('kim', 'pacmk'), ('b', 'blog'), ('c', 333), (123, 'name')])
    print(d.items())

    # items 하나씩 출력
    for i in d.items():
        print('i:{}'.format(i))
        print('key:{}'.format(i[0]))
        print('key:{}'.format(i[1]))

main()
