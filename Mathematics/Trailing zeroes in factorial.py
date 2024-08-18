def trailingZeroes(self, N):
    	#code here 
    	
    	res=0 #first the count of 5's will be 0
    	i=5  #initialize i with 5
    	#traverse till N
    	while(i<=N):
    	    res = res + N//i  #keep on dividing N by multiple of 5..
    	    i = i*5 #multiply i by 5
    	#At last return the value of res    
        return res
