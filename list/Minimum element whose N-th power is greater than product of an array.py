import math as m 
class Solution:
    # function to find the minimum element 
    def findMin(self, a, n): 
          
       #Complete the function
       
       #find the sum
        _sum=0
        for i in range(0,n):
            _sum+=m.log(a[i])
        
        #now taking exponentiation
        return int(m.exp(_sum/n))+1
