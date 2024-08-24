class Solution:    
    #Complete this function
    def printNos(self,N):
        #Your code here
        if(N==0):
            return
        self.printNos(N-1)
        print(N,end=" ")
        
    #     self.printNum(1,N)
    #     return
    # def printNum(self,i,N):
    #     if(i==N+1):
    #         return
    #     print(i,end=" ")
    #     self.printNum(i+1,N)
