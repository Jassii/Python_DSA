#User function Template for python3

class Solution:
    ##Complete this code
    def countOnes(self,arr, N):
        #Your code here
        #sort the array
        arr.sort()
        #left index
        leftIndex=self.left(arr,N,1)
        if(leftIndex==-1):
            return 0
        #right index
        rightIndex=self.right(arr,N,1)
        
        return rightIndex-leftIndex+1
    
    def left(self,arr,N,x):
        start=0
        end=N-1
        l=-1
        while(start<=end):
            mid=start+(end-start)//2
            if(arr[mid]==x):
                l=mid
                end=mid-1
            elif(arr[mid]>x):
                end=mid-1
            else:
                start=mid+1
        return l
    
    def right(self,arr,N,x):
        start=0
        end=N-1
        r=-1
        while(start<=end):
            mid=start+(end-start)//2
            if(arr[mid]==x):
                r=mid
                start=mid+1
            elif(arr[mid]>x):
                end=mid-1
            else:
                start=mid+1
        return r    
