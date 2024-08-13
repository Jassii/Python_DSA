#naive approach
# def lcm(a,b):
#     maxNum=max(a,b)
#     while(True):
#         if(maxNum%a==0 and maxNum%b==0):
#             return maxNum
#         else:
#             maxNum+=1


#Optimized approach -> a*b = lcm(a,b) * gcd(a,b)
def gcd(a,b):
    if(a==0):
        return b
    if(a>=b):
        return gcd(a%b,b)
    else:
        return gcd(b%a,a)
        
        
def lcm(a,b):
    return (a*b)//gcd(a,b)

if __name__=='__main__':
    a=int(input("Enter first number : "))
    b=int(input("Enter second number : "))
    value = lcm(a,b)
    print("LCM of {} and {} is {}".format(a,b,value))
