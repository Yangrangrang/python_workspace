'''
    중첩 if 문 : if문 안에 또 다른 if문 존재
'''


def main():
    pocket = ['paper', 'cellphone']
    card = True

    if 'money' in pocket :
        print("택시타고가세요")
    else :
        if card :
            print("else 택시를 타고가세요")
        else:
            print("걸어가세요")


main()
