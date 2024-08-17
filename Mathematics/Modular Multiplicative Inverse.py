class Solution:    
    ##Complete this function
    def modInverse(self,a,m):
        ##Your code here
        
        for x in range(0,m):
            value = (a*x)%m
            if(value==1):
                return x
        return -1  
