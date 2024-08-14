#not an optimized way to solve this question
import math
def primeFactors(n):
    for i in range(2,n+1):
        #check for factor as well as prime.
        
        #if it is not a factor
        if(n%i!=0):
            continue
        
        #check for prime
        prime=isPrime(i)
        if(prime==False):
            continue
        
        #now number is both factor and prime
        # print(i)
        
        #Now for how many times it should be repeated??
        x=n
        while(x%i==0): #divide the n/x by i and print i, until it is not divisible
            print(i)
            x=x//i
            

def isPrime(n):
    count=0
    for i in range(1,int(math.sqrt(n))+1):
        if(n%i==0):
            count+=1
            if(n%i!=i):
                count+=1
    if(count==2):
        return True
    return False


if __name__=='__main__':
    n=int(input("Enter number : "))
    primeFactors(n)
