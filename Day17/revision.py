#Task1
# amount=[45,120,89,210,95]
# new_list=[]
# for i in amount:
#     print(i)
#     if i>=100:
#         new_list.append(i)
# print(new_list)       


# Task2
customer ={"name":"Vandana","tier":"gold"}
print(customer["name"])
try :
 discount=(customer["discount"])
except KeyError :
 discount=0.0
print(f"discount is {discount}")