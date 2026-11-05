# num=set()
# num.add(10)
# num.add(20)
# num.add(30)
# print(num)
# print(hash(10))
# print(hash(20)==hash(10))

# print(hash("vandana"))
# print(hash(None))
# print(True)

# set={1,2,"Vandana",3.5,(1,2,3)}
# print(hash(set))

# list=[1,2,"Vandana",3.5,(1,2,3)]
# print(hash(list))  # This will raise an error because lists are mutable and not hashable

point={(1,2),(3,4)}
point.add((6,7))
print(point)
print(hash((10,20)))
print(hash(point))
