class MyClass:
    def __eq__(self, other):
        return True

myclass = MyClass()

if myclass is MyClass:
    print("myclass is MyClass with is keyword")
else:
    print("myclass is NOT MyClass with is keyword")

if myclass == MyClass:
    print("myclass is MyClass with == keyword")
else:
    print("myclass is NOT MyClass with == keyword")


if myclass is None:
    print("myclass is None with is keyword")
else:
    print("myclass is not None with is keyword")

if myclass == None:
    print("myclass is None with == keyword")
else:
    print("myclass is not None with == keyword")

#myclass is NOT MyClass with is keyword
#myclass is MyClass with == keyword
#myclass is not None with is keyword
#myclass is None with == keyword

"""Поэтому нужно проверять на None с помощью ключевого слова is.
А ещё (для некоторых классов) вызов метода __eq__ может занимать
много времени, и is будет просто-напросто быстрее."""