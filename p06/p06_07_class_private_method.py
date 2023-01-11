'''

'''
class Person:
    def __greeting(self):
        print('Hello')
    def hello(self):
        self.__greeting()

def main():
    james = Person()
    # james.__greeting()
    james.hello()

main()
