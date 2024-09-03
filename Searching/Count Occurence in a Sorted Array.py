def countOccurence(arr,x):
    #get its first occurence.
    first = firstIndex(arr,x)
    if(first==-1):#if first is -1, then it means that number is not present
        return 0
    last = lastIndex(arr,x)
    count = last-first+1
    return count

def lastIndex(arr,x):
    start=0
    end=len(arr)-1
    last=-1
    while(start<=end):
        mid=start+(end-start)//2
        if(arr[mid]==x):
            last=mid
            start=mid+1
        elif(arr[mid]<x):
            start=mid+1
        else:
            end=mid-1
    return last
    
def firstIndex(arr,x):
    start=0
    end=len(arr)-1
    first=-1
    while(start<=end):
        mid=start+(end-start)//2
        if(arr[mid]==x):
            first=mid
            end=mid-1
        elif(arr[mid]<x):
            start=mid+1
        else:
            end=mid-1
    return first        

if __name__=='__main__':
    l=input("Enter number space separated : ")
    arr = [int(num) for num in l.split(" ")]
    x=int(input("Enter the number : "))
    count=countOccurence(arr,x)
    print("Count of number {} is {}".format(x,count))
