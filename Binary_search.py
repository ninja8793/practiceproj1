list =[2,3,4,5,6,7]
n=2
def search(list,n):
    l =0
    u = len(list)-1
    while l<=u:
        mid = (l+u)//2
        if list[mid]==n:
            print("Element found at {} pos.".format(mid))
            break
        else:
            if list[mid]<n:
                l=mid+1
            else:
                u=mid-1
search(list,n)