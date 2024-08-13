def lcm(a,b):
    maxNum=max(a,b)
    while(True):
        if(maxNum%a==0 and maxNum%b==0):
            return maxNum
        else:
            maxNum+=1

if __name__=='__main__':
    a=int(input("Enter first number : "))
    b=int(input("Enter second number : "))
    value = lcm(a,b)
    print("LCM of {} and {} is {}".format(a,b,value))
