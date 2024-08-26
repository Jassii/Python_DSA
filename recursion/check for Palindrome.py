#check if a string is palindrome using recursion
def isPalindrome(n,start,end):
    #base case
    if(start>=end):
        return True
    return ((n[start]==n[end]) and isPalindrome(n,start+1,end-1))    

if __name__=='__main__':
    n=input("Enter sting to check: ")
    res = isPalindrome(n,0,len(n)-1)
    if(res==True):
        print("Yes it is a palindrome string.")
    else:
        print("It is not a palindrome string.")

#another method using reverse function (basic)
# def reverseString(n,size):
#     if(size==0):
#         return ""
#     return n[size-1]+reverseString(n,size-1)    
    

# if __name__=='__main__':
#     n=input("Enter sting to check: ")
#     res = reverseString(n,len(n))
#     if(res==n):
#         print("Yes it is a palindrome string.")
#     else:
#         print("It is not a palindrome string.")
