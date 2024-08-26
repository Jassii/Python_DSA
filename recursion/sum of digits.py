#sum of digits using recursion
def sumOfDigits(n):
    #you need to stop when you have a single digit number
    if(n<10):
        return n
    return n%10 + sumOfDigits(n//10)    

if __name__=='__main__':
    n=int(input("Enter number : "))
    res = sumOfDigits(n)
    print("Sum of Digits is ",res)
