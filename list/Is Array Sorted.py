class Solution:
    def isSorted(self,arr,n):
        #code here
        
        #base case
        #array will be sorted
        if(n==1):
            return 1
            
        #now array will be having more than 1 element
        #check if it array is in ascending order or descending order
        #because on the basis of that, will be applying the condition
        
        #If first element is less than equal to last element
        if(arr[0]<=arr[n-1]):
            #ascending order
            for i in range(0,n-1):
                if(arr[i]>arr[i+1]):
                    return 0
        elif(arr[0]>arr[n-1]): #if the first element is greater than the last element
            #decreasing order
            for i in range(0,n-1):
                if(arr[i]<arr[i+1]):
                    return 0
        
        #array is sorted so return -1
        return 1
