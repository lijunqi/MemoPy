
class TracingMeta(type):

# __prepare__ is a fundamental change in Python3.
#    @classmethod
#    def __prepare__(mcs, name, bases, **kwargs):
#        print("TracingMeta.__prepare__(name, bases, **kwargs)")
#        print("  mcs = ", mcs)
#        print("  name = ", name)
#        print("  bases = ", bases)
#        print("  kwargs = ", kwargs)
#        namespace = super().__prepare__(name, bases)
#        print("<-- namespace = ", namespace)
#        print()
#        return namespace

    def __new__(mcs, name, bases, namespace, **kwargs):
        print("TracingMeta.__new__(mcs, name, bases, namespace, **kwargs)")
        print("  mcs = ", mcs)
        print("  name = ", name)
        print("  bases = ", bases)
        print("  namespace = ", namespace)
        print("  kwargs = ", kwargs)
        cls = super(TracingMeta, mcs).__new__(mcs, name, bases, namespace)
        print("<-- cls = ", cls)
        print()
        return cls

    def __init__(cls, name, bases, namespace, **kwargs):
        print("TracingMeta.__init__(cls, name, bases, namespace, **kwargs)")
        print("  cls = ", cls)
        print("  name = ", name)
        print("  bases = ", bases)
        print("  namespace = ", namespace)
        print("  kwargs = ", kwargs)
        super(TracingMeta, cls).__init__(name, bases, namespace)
        print()


#class Widget(metaclass=TracingMeta):
class Widget(object):
    __metaclass__=TracingMeta
    def action(msg):
        print(msg)
    the_answer = 42
