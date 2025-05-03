arr = [1,3,6,14,17,19,24,25,36,38,39,43,45]
s = 0
def binarySearch(arr,n):
    global s
    if len(arr)<1:
        return -1
    if arr[len(arr)//2] > n:
        return binarySearch(arr[0:len(arr)//2],n)
    elif arr[len(arr)//2] < n:
        s = s+len(arr)//2+1
        return binarySearch(arr[(len(arr)//2+1):],n)
    else:
        return s+len(arr)//2
