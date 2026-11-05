# def student(**kwargs):
#     print(kwargs)
#     print(kwargs["Name"])
#     print(kwargs["age"])
#     print(kwargs["city"])
# student(Name="vandana",age=23,city="bangalore")


# def show_details(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key}={value}")
# show_details(Name="vandana",age=23,city="bangalore")

# def show(*args, **kwargs):
#     print("Positional:",args)
#     print("Keyword:",kwargs)
# show(10,20,30,name="Vandana",age=20)

# Order of Parammaters

# def example(name,*args,**kwargs):
#     print(name)
#     print(args)
#     print(kwargs)
# example("Vandana",12,24,30,age=23,city="Bangalore")


# numbers=[10,20,30]
# print(*numbers)
# print(numbers[0])

# numbers2=(40,50,60)
# print(*numbers2)
# print(numbers2[0])

# details={"name":"Vandana","age":23}
# print(*details)
# print(**details)

def student(name, age):
    pass
details = {"name": "Vandana", "age": 23}
student(*details)
student(**details)