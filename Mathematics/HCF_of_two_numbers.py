#Optimized Euclidean Algorithm
def gcd(a,b):
    if(a==0): 
        return b
    if(a>=b):
        return gcd(a%b,b)
    else:
        return gcd(b%a,a)


if __name__=='__main__':
    a=int(input())  #Enter the first number
    b=int(input())  #Enter the second number
    value = gcd(a,b)
    print("HCF of {} and {} is {}".format(a,b,value))
