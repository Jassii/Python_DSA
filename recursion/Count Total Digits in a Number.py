def countDigits(self, n):
        #base case
        if(n<10):
            return 1
        return 1 + self.countDigits(n//10)    
