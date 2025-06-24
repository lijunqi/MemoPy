class Singleton:

    _instance = None 

    def __new__(cls): 
        if not cls._instance: 
            cls._instance = super().__new__(cls)  
        return cls._instance
    
    # override the __init__ method to control initialization
    def __init__(self): 
        print('<init> called...')

