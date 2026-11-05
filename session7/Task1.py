# Task - 1
def access_vault(user_id, /, *, pincode, biometric_id=None):
    """Authenticate a user using keyword-only credentials.

    Args:
        user_id (int): Unique identifier of the user.
        pincode (str): Primary security PIN.
        biometric_id (str | None): Optional secondary biometric identifier.

    Returns:
        bool: True when the supplied credentials are accepted.
    """
    if not user_id or not pincode:
        return False

    if biometric_id is not None and not biometric_id:
        return False

    return True

print(access_vault(101, pincode="1234"))
print(access_vault(0, pincode="1234"))
print(access_vault(101, pincode="1234", biometric_id="BIO123"))