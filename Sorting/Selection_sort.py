def selection_sort(arr):
    print("In selection_sort function")
    print(arr)
    n=len(arr)
    for i in range(0,n):
        min_index=i
        #now traverse the array after i, and check for the minimum value index..
        for j in range(i+1,n):
            if(arr[j]<=arr[min_index]):
                min_index=j
        #found the minimum index position from i index..
        arr[i],arr[min_index] = arr[min_index],arr[i]
    return arr    
    
if __name__=="__main__":
    arr=[0,3,1,5,0]
    print("In main method")
    arr = selection_sort(arr)
    print(arr)
