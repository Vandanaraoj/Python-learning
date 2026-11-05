student={"names":["a","b","c"],"age":[12,34,56]}
print(student)
print(student["names"])
print(student["names"][0])
print(student["names"][0],student["age"][0])

length_list=len(student["names"])
print(length_list)

for i in range(length_list):
    print(student["names"][i],student["age"][i])