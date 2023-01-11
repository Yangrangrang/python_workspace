'''
    나이를 입력 받아
    if age >= 100 :
        초고령
    elif age >= 60 :
        고령
    elif age >= 40  :
        중년
    elif age >= 20 :
        청년
    else
        미성년
'''


def main():
    age = int(input("나이를 입력하세요>"))
    print("age:{}, type(age):{}".format(age, type(age)))

    if age >= 100 :
        print("초고령")
    elif age >= 60 :
        print("고령")
    elif age >= 40 :
        print("중년")
    elif age >= 20 :
        print("청년")
    else :
        print("미성년")

main()
