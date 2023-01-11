'''
문자열에 여러줄 출력
'''


def main():
    multiline = "Life is too short\nYou need Python"
    print("multiline:{}".format(multiline))

    multiline = ''' Life is too short
    You need Python
    '''
    print("multiline:{}".format(multiline))

    multiline = """ Life is too short
    You need Python
    """
    print("multiline:{}".format(multiline))

main()
