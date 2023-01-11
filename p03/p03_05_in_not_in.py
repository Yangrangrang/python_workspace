'''
만약 주머니 안에 돈이 있으면 택시를 타고가라
'''


def main():
    pocket = ['paper', 'cellphone', 'money']

    print("pocket in :{}".format('money' in pocket))    # pocket in :True

    if 'money' in pocket :
        print("택시를 타고가라")
    else :
        print("걸어가라")


main()
