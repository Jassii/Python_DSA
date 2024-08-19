ef insertAtIndex(self, arr, sizeOfArray, index, element):
        #your code here
        
        #without using function..
        
        #insert at the last position
        if(index==sizeOfArray-1):
            arr.insert(index,element)
            return arr
        
        #traverse from the back and check for the index value, if it matches
        #input the element (and right shift all the values to the right)
        
        arr.append(-1)
        for i in range(sizeOfArray-1,-1,-1):
            if(i==index):
                arr[i]=element
                return arr
            arr[i]=arr[i-1]
        
        return arr    
            
        
        
        #using function
        # arr.insert(index,element)
        # return arr
