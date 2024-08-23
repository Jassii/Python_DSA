my_list_str = input("Enter numbers with space ")
l = [int(num) for num in my_list_str.split()]
print("List is : ",l)

#without the use of function

#get the max element from the list.
if(len(l)<=1):
    print("No Second largest element is there")
    exit()

fmax=l[0]
n=len(l)
for i in range(1,n):
    if(l[i]>fmax):
        fmax=l[i]

print("First max element is ",fmax)

#now need to find second max
smax=None
for x in l:
    if(x!=fmax):
        if(smax==None):
            smax=x
        else:
            smax=max(smax,x)

#now i will have second max element
print("Second largest element is ",smax)
    
    

#with the help of sort function...

# #Now i have the list, my task is to find the second largest element in the list.
# l.sort() #sort the list.
# print("Sorted List is : ",l)

# found=False
# for i in range(len(l)-1,0,-1):
#     if(l[i-1]<l[i]):
#         #i found the second largest element.
#         print("Second largest element is ",l[i-1])
#         found=True
#         break
# if(found==False):
#     print("Second largest element is not found")
