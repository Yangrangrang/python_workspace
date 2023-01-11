'''

'''


def main():
    try:
        a = [1,2]
        # print(a[3])
        # IndexError:list index out of range
        # 4/0
        # ZeroDivisionError:division by zero
    except ZeroDivisionError as e:
        print('ZeroDivisionError:{}'.format(e))
    except IndexError as e:
        print('IndexError:{}'.format(e))



main()
