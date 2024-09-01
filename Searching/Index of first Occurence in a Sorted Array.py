def firstOccurence(arr,x,start,end):
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
    #if the number is not found
    return first

if __name__=='__main__':
    l=input("Enter the number space separeted : ")
    arr = [int(num) for num in l.split(" ")]
    x=int(input("Enter the number : "))
    firstIndex = firstOccurence(arr,x,0,len(arr)-1)
    print("First Occurence of the number {} is at index {}.".format(x,firstIndex))
