class Solution:
    def sumUnderModulo(self,a,b):
        # code here
        sum = (a+b)%(10**9 + 7)  #doing this modulo because, the sum can be very large, hence it was mentioned in the problem
        return sum
