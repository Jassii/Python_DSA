# Sieve of Eratosthenes
import math
def getPrime(n):
    
    #base case
    if(n<=1):
        #no prime numbers are there
        return 
    
    #take a boolean list having True value upto n+1 (inorder to include 0)
    check = [True]*(n+1)
    print("Old Boolean list",check)
    
    #trying something else (more efficient way)
    #traverse till sqrt of n..
    for i in range(2,int(math.sqrt(n))):
        #check if it is prime, or else dont go inside
        if(check[i]==True):
            #make factors of i(excluding i itself) to be False (start from its double)..will be increasing i by i(double)
            for j in range(2*i,n+1,i):
                check[j]=False
    
    
    #now traverse from 2, as the minimum prime number starts with 2..and make multiples of 2,3 and 5 to be False
    # for i in range(2,n+1):
    #     if(i==2 or i==3 or i==5):
    #         continue
    #     #check if it is divisible by 2 or 3 or 5 and make its position value to be False
    #     if(check[i]==True and (i%2==0 or i%3==0 or i%5==0)):
    #         check[i]=False
    
    
    #updated check list
    print("Updated Boolean list",check)
    
    #now traverse the check list and prine those values whose value is True(they arr prime numbers)
    for i in range(2,n+1):
        if(check[i]==True):
            print(i,end=" ")


if __name__=='__main__':
    n = int(input("Enter the number : "))
    getPrime(n)
