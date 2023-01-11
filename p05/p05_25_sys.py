'''
dos창에서 파람 전달
'''
import sys

def main():
    args = sys.argv[1:]

    for i in args:
        print(i.upper(), end=" ")


main()
