def recursiveSum(self,n):
        #code here
        if(n==0):
            return 0
        return n+self.recursiveSum(n-1)
