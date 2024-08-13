#User function Template for python3
import math
class Solution:
    def digitsInFactorial(self,N):
        # code here
        count=0
        for i in range(1,N+1):
            count+=math.log(i,10)
        return int(count)+1    
