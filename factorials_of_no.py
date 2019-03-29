def fact(n):

    f =1

    for i in range(1,n+1):
        f = f*i
    print("factorials of {} is :{}".format(n,f))
no = 5
result = fact(no)


# Usin Recursion ..................

def rfact(n):
    if n==0:
        return 1
    return n * rfact(n-1)


Rresult = rfact(5)
print("Recursion Fact:",Rresult)