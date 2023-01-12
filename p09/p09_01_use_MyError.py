'''

'''
# __str__ : 오류메세지를 출력 했을 때 메시지를 보이게 한다.
class MyError(Exception):
    def __str__(self):
        return "허용되지 않은 별명입니다."

def say_nick(nick):
    if nick == '바보':
        raise MyError()

    print("nick:{}".format(nick))

def main():
    try:
        say_nick('천사')
        say_nick('바보')
        # TypeError: 'module' object is not callable
    except MyError as e:
        print(e)

main()
