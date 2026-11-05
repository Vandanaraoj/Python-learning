x=100 # Outside a function, it is a global variable
def test():
    x=200
    print(x)  # Inside the function, it is local variable, so it will print 200
test()
print(x)

y=300 # Outside a function, it is a global variable
def test():
    print(y)  # if local value is not defined, it will print the global variable value
test()
print(y)