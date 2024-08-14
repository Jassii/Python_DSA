import math
class Solution:
    def isPrime(self,N):
        # code here
        count=0
        for i in range(1,int(math.sqrt(N))+1):  #will be traversing till sqrt of N, because after that it is just simply repeating
            if(N%i==0):
                count+=1
                if(N%i!=i):  #inorder to avoid same number like N is 36, hence 6 * 6 (avoiding such cases)
                    count+=1
        if(count==2):  #at last if the count is 2, it will be a prime number otherwise not.
            return True
        return False    
