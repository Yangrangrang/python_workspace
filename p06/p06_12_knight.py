'''

'''

class Knight:
    __item_limit = 10   # 비공개 클래스 변수(속성)

    def print_item_limit(self):
        print(Knight.__item_limit) # 클래스 내에서만 접근

def main():
    k = Knight()

    k.print_item_limit()    #10

    # type object 'Knight' has no attribute '__item_limit'. Did you mean: 'print_item_limit'?
    # Knight.__item_limit # 클래스 밖에서는 접근 불가


main()
