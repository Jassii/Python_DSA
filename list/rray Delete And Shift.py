def deleteFromArray(arr,n,idx):
    #code here
    #traverse from the index position till the second last index 
    for i in range(idx,n-1):
        arr[i]=arr[i+1]
    
    #make the last index value to be zero
    arr[n-1]=0
