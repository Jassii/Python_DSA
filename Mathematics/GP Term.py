class Solution:    
    #Compelte his function
    def termOfGP(self,A,B,N):
        #Your code here
        #base case
        if(N==1):
            return A
        if(N==2):
            return B
            
        #calculate the ratio
        r = B/A
        res = A*self.getPower(r,N-1)  #calculating the power in O(log N) TC
        return res #return the result
    
    #function to calcluate the power i.e. (a^b)
    def getPower(self,a,b):
        #base case
        if(b==0):
            return a
        value=1
        while(b>0):
            #if power is odd
            if(b&1):
                value = value*a
            
            a = a*a
            b = b>>1
        return value
