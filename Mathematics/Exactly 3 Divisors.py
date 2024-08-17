import math
class Solution:
  #just traverse till sqrt(N), and find the prime number counts...and return the count
    def exactly3Divisors(self,N):
        count=0
        for i in range(2,int(math.sqrt(N))+1):
            if(self.isPrime(i)==True):
                count+=1
        return count        
        
    #more optimized way to check if the number is prime or not.
    def isPrime(self,n):
        for i in range(2,int(math.sqrt(n))+1):
            if(n%i==0):
                return False
        return True 
