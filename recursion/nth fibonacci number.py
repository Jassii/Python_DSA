def fibonacci(n):
    #some base cases
    if(n==0):
        return 0
    elif(n==1):
        return 1
    return fibonacci(n-1)+fibonacci(n-2)
    
if __name__=='__main__':
    n=int(input("Enter the number : "))
    value = fibonacci(n)
    print("Nth Fibonacci number is ",value)
