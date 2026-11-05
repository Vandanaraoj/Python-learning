Student =[{"name" :"Vandana","age":28,"marks":87}]
print(Student)
print(Student[0]["name"])  #Indexing should be given since dictionary in inside a list
print(Student[0]["age"])

Student1 =[{"name" :"Spandana","age":28,"marks":87},{"name" :"Rao","age":43,"marks":65}]
print(Student1)
print(Student1[1])
print(Student1[0]["name"])

Student2=[{"name" :"Skanda","age":32,"marks":33},{"name" :"Shreya","age":33,"marks":65},{"name" :"Rao","age":43,"marks":34}]

length=len(Student2)
print(length)

for i in range (length) :
  print(Student2[i]["name"])

for studentData in range (Student2):
  print(studentData[Student2])