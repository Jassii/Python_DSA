import math
def allDivisors(n):
    for i in range(1,int(math.sqrt(n))+1):
        if(n%i==0):  #with the help of this, i will be able to print one value of my pair.
            print(i)  
            #inorder to print other value of my pair
            if(n//i!=i):  #doing this because I dont want my both the values to be same..
                print(n//i)

if __name__=='__main__':
    n=int(input("Enter number : "))
    allDivisors(n)
