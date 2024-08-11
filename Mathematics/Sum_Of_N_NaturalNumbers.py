#input the number
n=int(input("Enter n: "))
#need to get the sum till n natural numbers

#First Case
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)

#Second Case
value = n*(n+1)/2
print(value)
