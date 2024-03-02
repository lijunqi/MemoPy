from inspect import signature

def my_func(
        a,
        b: int = 1,
        c=2,
        *args,
        kw1,
        kw2=100,
        kw3=200,
        **kwargs) -> None:
    """ This function does nothing but does have various parameters and annotations. """
    i = 10
    j = 20

print("my_func.__name__        : ", my_func.__name__) # my_func
print("my_func.__doc__         : ", my_func.__doc__)
print("my_func.__annotations__ : ", my_func.__annotations__) # {'b': <class 'int'>, 'return': None}
print("my_func.__defaults__    : ", my_func.__defaults__)    # (1, 2)
print("my_func.__kwdefaults__  : ", my_func.__kwdefaults__)  # {'kw2': 100, 'kw3': 200}

print("my_func.__code__.co_name    : ", my_func.__code__.co_name) # my_func
print("my_func.__code__.co_varnames: ", my_func.__code__.co_varnames) # ('a', 'b', 'c', 'kw1', 'kw2', 'kw3', 'args', 'kwargs', 'i', 'j')
print("my_func.__code__.co_argcount: ", my_func.__code__.co_argcount) # 3

sig = signature(my_func)
print("sig type: ", type(sig)) # <class 'inspect.Signature'>
print("sig.parameters type: ", type(sig.parameters)) # <class 'mappingproxy'>
for k, param in sig.parameters.items():
    print('Key       : ', k)
    print('Name      : ', param.name)
    print('Default   : ', param.default)
    print('Annotation: ', param.annotation)
    print('Kind      : ', param.kind)
    print('------------------------------')
"""
Key       :  a
Name      :  a
Default   :  <class 'inspect._empty'>
Annotation:  <class 'inspect._empty'>
Kind      :  POSITIONAL_OR_KEYWORD
------------------------------
Key       :  b
Name      :  b
Default   :  1
Annotation:  <class 'int'>
Kind      :  POSITIONAL_OR_KEYWORD
------------------------------
Key       :  c
Name      :  c
Default   :  2
Annotation:  <class 'inspect._empty'>
Kind      :  POSITIONAL_OR_KEYWORD
------------------------------
Key       :  args
Name      :  args
Default   :  <class 'inspect._empty'>
Annotation:  <class 'inspect._empty'>
Kind      :  VAR_POSITIONAL
------------------------------
Key       :  kw1
Name      :  kw1
Default   :  <class 'inspect._empty'>
Annotation:  <class 'inspect._empty'>
Kind      :  KEYWORD_ONLY
------------------------------
Key       :  kw2
Name      :  kw2
Default   :  100
Annotation:  <class 'inspect._empty'>
Kind      :  KEYWORD_ONLY
------------------------------
Key       :  kw3
Name      :  kw3
Default   :  200
Annotation:  <class 'inspect._empty'>
Kind      :  KEYWORD_ONLY
------------------------------
Key       :  kwargs
Name      :  kwargs
Default   :  <class 'inspect._empty'>
Annotation:  <class 'inspect._empty'>
Kind      :  VAR_KEYWORD
------------------------------
"""