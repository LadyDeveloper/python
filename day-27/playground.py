def add(*addn):
    total = 0
    for n in addn:
        total += n
    return total

add(7,14,20,30)

def calculate(n, **kwargs):
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    
    # print(kwargs["add"])
    # print(kwargs["multiply"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:
    
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = Car(make="Nissan")
print(my_car.make)