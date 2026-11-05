list=[59,60,65,65,68,70,72,75,75,76,77,81,82,84,87,90,95,98,99,100]
n = len(list)
print(n)
QA1 =int(((n)*1/4)) # (n)>> Even no.of.data and (n+1) for odd no.of.data
QA2= int(((n)*2/4))
QA3= int(((n)*3/4))
print(f"QA1: {QA1}")
print(f"QA2: {QA2}")
print(f"QA3: {QA3}")
print(list[QA1])
print(list[QA2])
print(list[QA3])