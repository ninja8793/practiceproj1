import time

user = "asd"
strlist = []
strset = set()
strdict = {}

srno = 1
for i in user:
    strlist.append(i)
    strset.add(i)
    strdict[user.index(i)] = i

    #time.sleep(0.30)
    print('{}.{} is added into list at position no :{}.'.format(srno,i,user.index(i)))
    srno+1

for i in range(0,5):
    #time.sleep(1)
    print("/")
print('String List:',strlist)
print('String Set:',strset)
print('String Dictionary:',strdict)


name = 'nitin gharge'
print(name)