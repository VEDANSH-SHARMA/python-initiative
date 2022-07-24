a=int(input("Number of elements in the array:"))
arr1=list(map(int, input("elements of array:").strip().split()))
print(arr1)
size = len(arr1)
def array_mean(a,l):
    sum = 0
    for i  in range(0,l):
        sum +=a[i]
    
    return sum/l
    
meanofanarray = array_mean(arr1,len(arr1))
print ("mean of an array:",meanofanarray)