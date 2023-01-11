'''

'''


def main():
    f = open("/Users/yanghanna/Documents/BIG_AI0102/1. python/pcmk01.txt",'r')
    lines = f.readlines()   #list return

    for line in lines:
        print(line.rstrip('\n'))

    f.close()
main()
