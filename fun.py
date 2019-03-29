import time
class Funct:

    def fun5(self):
        time.sleep(1)
        print('In fun5...!')
        Funct.fun1(self)

    def fun4(self):
        time.sleep(1)
        print('In fun4...!')
        Funct.fun5(self)

    def fun3(self):
        time.sleep(1)
        print('In fun3...!')
        Funct.fun4(self)

    def fun2(self):
        time.sleep(1)
        print('In fun2...!')
        Funct.fun3(self)

    def fun1(self):
        time.sleep(1)
        print('In fun1...!')
        Funct.fun2(self)

o1 = Funct()
o1.fun1()