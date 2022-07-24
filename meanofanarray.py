arr1 = [4,5]
size = len(arr1)
def array_mean(a,l):
    sum = 0
    for i  in range(l):
        sum +=a[i]
    
    return sum/l
    
meanofanarray = array_mean(arr1,len(arr1))
print (meanofanarray)
