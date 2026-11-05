GUEST = 1
USER = 2
ADMIN = 4
SUPERUSER = 8

current_access = GUEST | USER

NEW_SECURE_LEVEL = ADMIN << 1

user_exists = current_access & USER

updated_access = current_access ^ GUEST

print(f"Current Access      : {current_access}  Binary : {bin(current_access)}")
print(f"New Secure Level    : {NEW_SECURE_LEVEL}  Binary : {bin(NEW_SECURE_LEVEL)}")
print(f"USER Check (&)      : {user_exists}  Binary : {bin(user_exists)}")
print(f"Updated Access (^ ) : {updated_access}  Binary : {bin(updated_access)}")