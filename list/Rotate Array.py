class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self,A,D,N):
        #Your code here
        
        #minimize the value of D
        D = D%N
        #passing the index in the parameters
        self.reverse(0,D-1,A)
        self.reverse(D,N-1,A)
        self.reverse(0,N-1,A)
        return A
    
    #reverse the array list
    def reverse(self,i,j,arr):
        while(i<=j):
            arr[i],arr[j] = arr[j],arr[i]
            i+=1
            j-=1
