class MyClass:
    def method(self):
        print('instance method called',self)

    @classmethod
    def classmethod(*cls):
        print('class method called',cls)

    @staticmethod
    def staticmethod():
        print('static method called')
'''
obj = MyClass()
print('***********obj calling***************')
obj.method()
obj.classmethod()
obj.staticmethod()
print('..........................')

MyClass.method(obj)
MyClass.classmethod()
MyClass.staticmethod()

#obj.method()
#MyClass.method(obj)
#obj.classmethod()
#MyClass.classmethod()
#print('...................................')
#MyClass.staticmethod()
#print('...................................')
'''
import math
import time
class Pizza:
    def __init__(self,radius,ingredients):
        self.radius = radius
        self.ingredients = ingredients

    def __repr__(self):
        return (f'Pizza({self.radius!r},'
                f'{self.ingredients})')

    def area(self):
        return self.circle_area(self.radius)

    @staticmethod
    def circle_area(r):
        print('radius:',r**2*math.pi)
        return r**2*math.pi




p = Pizza(4,['mozerala','tomatos'])
print(p)
p.area()
for i in range(1,10):
    time.sleep(2)
    Pizza.circle_area(i)