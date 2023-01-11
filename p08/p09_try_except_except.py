'''

'''


def main():
    try:
        a = [1,2]
        # print(a[3])
        # IndexError:list index out of range
        4/0
        # ZeroDivisionError:division by zero
    except(ZeroDivisionError,IndexError) as e:
        print(e)



main()
