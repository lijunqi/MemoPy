from datetime import datetime
from functools import wraps

########################################################################
def my_decorator(func):
    def wrapper():
        print("Enter wrapper")
        func()
        print("Leave wrapper")
    return wrapper

def say_whee():
    print("Whee!")

say_whee_v1 = my_decorator(say_whee)
say_whee_v1()

print('='*20)

# * Syntactic Sugar

@my_decorator
def say_whee_v2():
    print("Whee!")
say_whee_v2()

print('='*20)
########################################################################

def pre_date(pre):
    def date(func):
        def wrapper():
            func()
            date = datetime.utcnow()
            print(pre + str(date))
        return wrapper
    return date

@pre_date('Today is :')
def alan():
    print ('alan speaking')
    
@pre_date('I am Tom :')
def tom():
    print ('tom speaking')

alan()
tom()

#def pre_date_2(pre):
#    @wraps(pre)
#    def inner(*args, **kwargs):
#        print(f"before...")
#        func(*args, **kwargs)
#        print("after...")
#    return inner
#
#@pre_date_2('Date:')
#def jacky():
#    print('I am Jacky.')
#
#jacky()

print('=========')

###########################################################
# Not define a function in decorator
# register run before funcitons
# e.g register router in web framework
registry = []

def register(func):
    print('running register(%s)' % func)
    registry.append(func)
    return func


@register
def f1():
    print('running f1()')


@register
def f2():
    print('running f2()')


@register
def f3():
    print('running f3()')


def main():
    print('running main()')
    print('registry ->', registry)
    f1()
    f2()
    f3()

main()
