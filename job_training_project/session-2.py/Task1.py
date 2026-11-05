x = 256
y = 256

a = 257
b = 257

is_same_identity = a is b
is_same_value = a == b

status = None

print("\n================ TASK 1 ================\n")

print(f"""
x = {x}, id(x) = {id(x)}
y = {y}, id(y) = {id(y)}

a = {a}, id(a) = {id(a)}
b = {b}, id(b) = {id(b)}

a is b  : {is_same_identity}
a == b  : {is_same_value}

status      : {status}
type(status): {type(status)}
id(status)  : {id(status)}
""")