# def show(*args):
#     for value in args:
#         print(value)
#         print(args[0])
# show(10,20,30)


def student(name,*marks):
    print("Name",name)
    print("Marks",marks)
student("Rahul",45,43,23)