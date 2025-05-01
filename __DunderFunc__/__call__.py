class XConvert:
    # 定义__call__方法
    def __call__(self, name, number):
        print("In __call__(): ", name, number)
convert = XConvert()
print("Ready...")
convert("Tom", 123)

print("is callable:", callable(convert))
