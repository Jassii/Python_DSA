import math
def computePower(a,b):
    #optimized way without using funciton
    res=1
    while(b>0):
        #if the number is odd
        if(b&1):
            res = res * a
        a = a * a
        b = b>>1 #right shift by 1, it will divide b by 2 (b/2)
      
    return res    
    
    #optimized approach, we can use the function (TC - O(log n))
    # print(math.pow(x,n))
    
    #brute force approach
    #some base cases
    #if power is 0
    # if(n==0):
    #     print(1)
    #     return
    # #if power is 1
    # if(n==1):
    #     print(x)
    #     return
    
    # res=1
    # for i in range(1,n+1):
    #     res = res*x
    # print("Value is ",res)
    # return
    

if __name__=='__main__':
    a = int(input("Enter the number : "))
    b = int(input("Enter power : "))
    power = computePower(a,b)
    print("Result is ",power)
