class Solution:
    ##Complete the below codes
    #Function to find median of the array elements.
    def median(self,A,N):
        
        A.sort()
        
        ##Your code here
        #If median is fraction then convert the median to integer and return
        
        #if N is odd
        if(N%2!=0):
            median = (N+1)//2 #floor value
            return A[median-1]
        #if N is even
        else:
            # median = avg of (N/2)th term and (N/2+1)th term
            first = N//2
            second = N//2 + 1
            #average of the above two
            median = (A[first-1] + A[second-1])//2
            return median
                  
    #Function to find mean of the array elements.   
    def mean(self,A,N):
        ##Your code here
        sum=0
        for i in range(0,N):
            sum+=A[i]
        return sum//N #return the average/mean of the numbers
