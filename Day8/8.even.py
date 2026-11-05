numbers=[1,2,3,4,5,6,7]
even=[x for x in numbers if x%2==0]
print(even)

even=[]
for i in numbers:
    if i%2==0:
        even.append(i)
print(even)
