'''

'''


def main():
    a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
    print("-"*20)
    print('a:{}'.format(a))
    print("-"*20)

    print('a[2:5]:{}'.format(a[2:5]))
    # a[3][:2]:['a', 'b']
    print('a[3][:2]:{}'.format(a[3][:2]))


main()
