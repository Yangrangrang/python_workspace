'''

'''

class PcwkException(Exception): # 사용자 정의 예외 클래스
    def __init__(self,message, code):
        super().__init__(message)
        self.message = message
        self.code = code

    def __str__(self):
        return "message:{}, code:{}".format(self.message, self.code)

def p_func():
    raise PcwkException("사용자 정의 예외 발생", 10)

def main():
    try:
        p_func()

    except PcwkException as e:
        print("-"*35)
        print(e)
        print(e.message, e.code)
        print("-"*35)




main()
