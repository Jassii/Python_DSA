class Solution:
    #Function to find element with more appearances between two elements in an array.    
    def majorityWins(self, arr, n, x, y):
        # code here
        cx=0
        cy=0
        for i in range(0,n):
            if(arr[i]==x):
                cx+=1
            elif(arr[i]==y):
                cy+=1
        #now i will be having count of x and y..
        if(cx>cy):
            return x
        elif(cy>cx):
            return y
        
        #if both have the same count then return min of x and y
        return min(x,y)
