'''

'''


def main():
    d = {'a': 123321, 'kim': 'pacmk', 'b': 'blog', 'c': 333, 123: 'name'}

    # 값이 없을 때 접근
    r01 = d.get('ccc')
    print('r01:{}'.format(r01)) # r01:None

    r02 = d.get('a')
    print('r02:{}'.format(r02)) # r02:123321
    print("-"*35)
    for k in d.keys():
        print('key:{}, value:{}'.format(k,d.get(k)))
main()
'''
r01:None
r02:123321
-----------------------------------
key:a, value:123321
key:kim, value:pacmk
key:b, value:blog
key:c, value:333
key:123, value:name
'''
