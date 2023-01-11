'''

'''


def main():
    b = b'Python rules' # 바이트 상수
    print('b:{}, type:{}'.format(b, type(b)))   # b:b'Python rules', type:<class 'bytes'>

    # 문자열에서 사용하는 연산을 거의 지원한다.
    print('b[1:5]:{}'.format(b[1:5]))   # b[1:5]:b'ytho'
    print('b.upper():{}'.format(b.upper()))     # b.upper():b'PYTHON RULES'

    # 유니크도 문자
    s = '이상무'
    print('s:{}'.format(s))
    # SyntaxError: bytes can only contain ASCII literal characters
    # 1 바이트 문자만 표현
    #sb = b'이상무'

    # 바이트를 문자열로 : decode() : UTF-8
    #                decode('cp949')
    print(b.decode())
    print(b.decode('cp949'))

    # 한글 encoding
    s = '이상무'
    print('s:{}'.format(s))
    # s.encode():b'\xec\x9d\xb4\xec\x83\x81\xeb\xac\xb4'
    print('s.encode():{}'.format(s.encode()))

    # 변경 가능한 bytearray로 변환

    # b'Python rules' -> b'Python Rules'
    ba = bytearray(b)
    print('ord(a):{}'.format(ord('a')))
    ba[7] = ord('R')    # R영문자에 해당하는 아스키 코드 값으로 변환
    print("ba:{}".format(ba))


main()
