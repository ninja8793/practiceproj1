from functools import reduce
nums= [3,5,2,4,6,8,10]

name = ['a','s','c']

evens  = list(filter(lambda n:n%2==0,nums))
doubles=list(map(lambda n:n*2,evens))
sum = reduce(lambda a,b:a+b,doubles)
nsum = reduce(lambda a,b:a+b,name)

print(evens)
print(doubles)
print('sum of doubles:',sum)
print('concatination of name list:',nsum)