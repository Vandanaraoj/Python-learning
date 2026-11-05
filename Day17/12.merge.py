import pandas as pd
students = pd.DataFrame({'student_id': [101, 102,103],"name":["rahul","priya","arun"]})
marks=pd.DataFrame({"student_id": [101, 102,103],"math":[45,56,67]})
print(students)
print(marks)
result= pd.merge(students, marks, on='student_id')
print(result)