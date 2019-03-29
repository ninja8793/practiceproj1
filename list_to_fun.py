lst = [22,23,45,23,44,66]


def cal(lst):
    odd = 0
    even = 0
    for a in lst:
        if a % 2 == 0:
            print('even no:',a)
            even+=1
        else:
            print("odd:",a)
            odd+=1
    print("#####################################################################")
    print("even:",even)
    print("odd:",odd)
cal(lst)