list = [2,4,3,5,7,6,8]
n = int(input("Enter element you want to search:"))
pos = -1
print("#################")

def search(list,n):
    for i in range(0,len(list)):
        if list[i] == n:
            global pos
            pos=i
            return True

if search(list,n):
    print("Elemen {} found at {}^th Position".format(n,pos))
else:
    print("Element not found")
