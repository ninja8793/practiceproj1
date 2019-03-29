def sort(list):
    a = len(list)
    for i in range(a):
        minpos = i
        for j in range(i,a):
            if list[j]<list[minpos]:
                minpos = j
        temp = list[i]
        list[i] = list[minpos]
        list[minpos] = temp

        print(list)

list =[4,3,5,6,7,0,1]
sort(list)
print("List Sorted Successfully..!")