'''

'''

def avg_numbers(*args):
    sum = 0
    cnt = 0
    for i in args:
        sum += i
        cnt += 1
    return sum / cnt

def main():
    print(avg_numbers(1,2))
    print(avg_numbers(1,2,3,4,5))




main()
