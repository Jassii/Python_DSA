class Solution:   
    def peakElement(self,arr, n):
        # Code here
        #base case
        if(n==1):
            return 0
        
        #naive approach
        # if(arr[0]>=arr[1]):
        #     return 0
        # elif(arr[n-1]>=arr[n-2]):
        #     return n-1
        
        # for i in range(1,n-1):
        #     if(arr[i]>=arr[i-1] and arr[i]>arr[i+1]):
        #         return i
    
        # return -1            
        
        
        index=self.peak(arr,0,n-1)
        return index
        
    #recursive binary search approach
    def peak(self,arr,start,end):
        if(start<=end):
            mid=start+(end-start)//2
            #0th index
            if(mid==0 and arr[mid]>=arr[mid+1]):
                return mid
            #last index
            elif(mid==len(arr)-1 and arr[mid]>=arr[mid-1]):
                return mid
            #it is not at the edges
            elif(arr[mid]>=arr[mid-1] and arr[mid]>=arr[mid+1]):
                return mid
            elif(arr[mid+1]>arr[mid]): #if the right element is greater, peak element is at right side
                return self.peak(arr,mid+1,end)
            else:#peak element is at the left side
                return self.peak(arr,start,mid-1)
        return -1
