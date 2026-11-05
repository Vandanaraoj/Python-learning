# def outer():
#     message = "Hello"  # enclosing variable
#     def inner():
#         print(message)  # inner function can access the enclosing variable  
#     inner()
# outer()


a="Global variable"  # global variable
def outer():
    a="Enclosing variable"
    print(a)  # enclosing variable
    def inner():
        a="Local variable"  # local variable
        print(a)  # inner function can access the local variable  
    inner()
outer()    
print(a)  # global variable