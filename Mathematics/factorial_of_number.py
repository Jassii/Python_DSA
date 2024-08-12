#recursive approach
def fact(n):
    #base case
    if(n==0 or n==1):
        return 1
    return n*fact(n-1)


if __name__ == '__main__':
    n=int(input("Enter the number : "))
    value = fact(n)
    print("Factorial of a number {} is {}".format(n,value))
