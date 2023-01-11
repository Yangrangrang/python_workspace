'''

'''
# **kwargs: 딕셔너리가 되고 key = value 형태가 된다.
def print_kwargs(**kwargs):
    print(kwargs)

def main():
    print_kwargs(a = 1)
    print_kwargs(name = "python", age = 11)


main()
