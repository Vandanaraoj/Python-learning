number=[1,2,3,4]
result=["even" if x%2==0 else "odd" for x in number]
print(result)

number1=[-1,2,-3,4,0]
result1=["Positive" if x>=0 else "negative" for x in number1]
print(result1)

words=["python","is","very","powerful","language"]
result3=[word for word in words if len(word)>5]
print(result3)