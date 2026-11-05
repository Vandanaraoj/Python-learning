def outer():
    print("This is outer function")  #enclosing variable
    def inner():
        print("This is inner function")
    inner()
outer()


def test(s, t):
    print(s+t)
    def inner():
        print("This is inner function")
    inner()
test(10, 20)

def sample(s, t):
 return s+t
def inner():
    print("This is inner function")
    inner()
sample(10, 20)