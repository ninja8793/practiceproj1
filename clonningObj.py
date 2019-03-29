from collections import namedtuple
xs = [[1,2,3],[4,5,6]]

print('origanal xs:',xs)

ys = list(xs)

print('copied into ys:',ys)
xs[1][0] = 'X'
print('updated xs:',xs)
print('update into ys:',ys)

xs.append([7,8,9])
print('appended xs:',xs)

print('after append in xs ..ys will be:',ys)

xs.clear()
print('after clear xs:',xs)
print('after clear xs ..ys will be:',ys)


car = namedtuple('car','color mileage')
print('type of car:...',car.__doc__)

sp='1 2 3'.split()
print('split fun:..',sp)





