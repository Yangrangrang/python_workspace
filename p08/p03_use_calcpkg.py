'''

'''

import calcpkg.operation    # calcpkg 패키지의 operation 모듈 가져옴
import calcpkg.geometry     # clacpkg 패키지의 geometry 모듈 가져옴

def main():
    print('calcpkg.operation.add(10,20):{}'.format(calcpkg.operation.add(10,20)))
    print('calcpkg.operation.mul(10,20):{}'.format(calcpkg.operation.mul(10,20)))

    print('-'*35)
    print('calcpkg.geometry.triangle_area(30,40):{}'.format(calcpkg.geometry.triangle_area(30,40)))
    print('calcpkg.geometry.rectangle_area(30, 40):{}'.format(calcpkg.geometry.rectangle_area(30, 40)))

main()
