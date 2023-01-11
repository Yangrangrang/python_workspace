'''

'''

class Person:
    '''사람 클래스'''

    def greeting(self):
        '''greeting 메서드'''
        print('Hello')

def main():
    print('Person.__doc__:{}'.format(Person.__doc__))
    print('Person.greeting.__doc__:{}'.format(Person.greeting.__doc__))

    mari = Person()
    print(mari.greeting.__doc__)

main()
'''
Person.__doc__:사람 클래스
Person.greeting.__doc__:greeting 메서드
greeting 메서드
'''
