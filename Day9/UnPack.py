def numbers2(b,a):
    """This function will add and multiply 2 no's and return the result
    This Function takes 2 arguments
    The output of the function is Integer
    Type error if the output in not integer"""
    return (a+b,a*b)

Answer=numbers2(2,3)
print(Answer)
a,b=Answer
print(numbers2.__doc__)
print("Add:", a)
print("Product:", b)
help(numbers2)