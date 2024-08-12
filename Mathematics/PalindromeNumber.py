n=int(input("Enter the number: "))

#check if the number is palindrome or not
rev=0
t=n
while(t>0):
    ld = t%10
    rev = rev*10 + ld
    t=t//10

if(rev==n):
    print("Number {} is a palindrome number".format(n))
else:
    print("Number {} is not a palindrome number".format(n))
