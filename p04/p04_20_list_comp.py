'''
new_list = [변수 활용 for 변수 in 반복대상 if 조건]
'''


def main():
    products = ['GOOD-2022', 'GOOD-2023', 'BAD-2022', 'BAD-2023']
    recall = [] # BAD로 시작하는 제품 추출

    for p in products:
        if p.startswith('BAD'):
            recall.append(p)
    print("-"*35)
    print('recall:{}'.format(recall))
    print("-" * 35)

    # new_list = [변수 활용 for 변수 in 반복대상 if 조건]
    pcmk_list = [x for x in products if x.startswith('BAD')]
    # pcmk_list:['BAD-2022', 'BAD-2023']
    print('pcmk_list:{}'.format(pcmk_list))

    m_list = [1,2,3,4,5]
    # 3보다 큰 수의 곱하기 2를 해서 할당
    new_list = [x * 2 for x in m_list if x>3]
    print(new_list)

    # 번째 해서 할당! : str(정수)
    new_list2 = [str(x)+ '번째' for x in m_list]
    print(new_list2)
main()
