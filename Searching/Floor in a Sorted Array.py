class Solution:
    #User function Template for python3
    
    #Complete this function
    def findFloor(self,A,N,X):
        #Your code here
        start=0
        end=N-1
        res=-1
        while(start<=end):
            mid=start+(end-start)//2
            if(A[mid]==X):
                return mid
            elif(A[mid]<X):
                res=mid
                start=mid+1
            else:
                end=mid-1
        
        return res        
