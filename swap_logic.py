#first way.........possible in all lang
a = int(input("Enter A:"))
b = int(input("Enter B:"))

a = a+b
b =a-b
a =a-b
print("First Method...1")
print("A:{} and B:{}".format(a,b))

#second way.......Only in python lang possible
print("Second Method...2")
a,b = b,a
print("A:{} and B:{}".format(a,b))

