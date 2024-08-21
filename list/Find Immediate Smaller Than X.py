class Solution:
    def immediateSmaller(self,arr,n,x):
        #return required ans
        
        #code here
        
        #sort the array
        arr.sort()
        
        #traverse from the back and return the just smaller value from X
        for i in range(n-1,-1,-1):
            if(arr[i]<x):
                return arr[i]  #return the smaller and closest
        
        #if no value is smaller than X 
        return -1
