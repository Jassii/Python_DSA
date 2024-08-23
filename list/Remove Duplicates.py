my_list_str = input("Enter numbers with space ")
l = [int(num) for num in my_list_str.split()]
print("List is : ",l)

l.sort()
n=len(l)
#remove duplicates from the sorted array.

#more efficient way to solve this question
res=1
for i in range(1,n):
    if(l[i]!=l[res-1]):
        l[res]=l[i]
        res+=1
print(res)        
print(l)  


# temp=[0]*n #temporary array of size n.
# temp[0]=l[0]
# index=1 #index of the result array
# for i in range(1,n):
#     if(temp[index-1]!=l[i]):
#         temp[index]=l[i]
#         index+=1

# print("List after removing duplicates")

# #copy the temporary array to the orignal array/
# for i in range(0,n):
#     l[i]=temp[i]

# print("Original array without any dulicates is ",l)
