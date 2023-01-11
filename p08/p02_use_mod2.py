'''

'''
import mod2

def main():
    # 변수
    print('mod2.PI:{}'.format(mod2.PI))

    # 클래스 내 함수
    a = mod2.Math()
    print('a.solv(10):{}'.format(a.solv(10)))
    print(mod2.Math().solv(12))

    # 일반 함수
    print('mod2.add(11,13):{}'.format(mod2.add(11,13)))



main()
