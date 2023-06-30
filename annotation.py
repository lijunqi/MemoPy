def validate(func, locals):
    for k, v in func.__annotations__.items():
        print('k = %s, v = %s' %(k, v))
        value = locals[k]
        print('locals = %s' % locals)
        print('locals[%s] = %s' % (k, locals[k]))
        print('-------------\n')
#        try: 
#            pr=test.__name__+': '+test.__docstring__
#        except AttributeError:
#            pr=test.__name__   
#        msg = '{}=={}; Test: {}'.format(var, value, pr)
#        assert test(value), msg


def between(lo, hi):
    def _between(x):
            return lo <= x <= hi
    _between.__docstring__='must be between {} and {}'.format(lo,hi)       
    return _between

def f(x: between(3,10), y:lambda _y: isinstance(_y,int)):
    validate(f, locals())
    print(x,y)

print('__annotations__:\n%s\n' % f.__annotations__)
f(3, 5)


##################################################################
def kinetic_energy(m:'in KG', v:'in M/S')->'Joules': 
    return 1/2*m*v**2

print(kinetic_energy.__annotations__)
print(kinetic_energy.__annotations__['m'])
for k, v in kinetic_energy.__annotations__.items():
    print('k = %s, v = %s' %(k, v))

print('===============')
loc = locals()
print(type(loc))
print(loc)
print('===============')
print(loc.values())
#for v in loc.values():
#    print('locals v = %s' % (v))


print('@@@@@@@@@@@@@@@@')
def foo(x, y, z):
    print(locals())

foo(1,2,3)
