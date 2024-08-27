#apply binary search in the array.
def binarySearch(arr,x,start,end):
    mid=start+(end-start)//2
  #base condition
    if(start<=end):
        if(arr[mid]==x):
            return mid
        elif(arr[mid]<x):
            return binarySearch(arr,x,mid+1,end)
        else:
            return binarySearch(arr,x,start,mid-1)
    
    return -1 #if the element is not found    

if __name__=='__main__':
    l = input("Enter the number with space : ").split()
    arr = [int(num) for num in l] #list has been taken 
    #sort the list as for binary seacrh array should be in sorted order.
    arr.sort()
    print("Array after sorting is : ",arr)
    x = int(input("Enter the number which has to be found : "))
    index = binarySearch(arr,x,0,len(arr)-1)
    if(index==-1):
        print("Element not found. Sorry!")
        exit()
    print('Element {} is found at {} index position.'.format(x,index))
