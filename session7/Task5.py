def validate_account_status(account_id):

    print("\n--- Task 5: Account Validation Wrapper ---")

    if account_id == "ACC101":

        status_code = 200
        is_active = True
        kyc_complete = True

    elif account_id == "ACC102":

        status_code = 200
        is_active = True
        kyc_complete = False

    else:

        status_code = 404
        is_active = False
        kyc_complete = False

    return status_code, (is_active, kyc_complete)


status_code, (is_active, kyc_complete) = validate_account_status("ACC101")

print("Status Code:", status_code)
print("Account Active:", is_active)
print("KYC Complete:", kyc_complete)


# Single-line nested unpacking

_, (_, kyc_complete) = validate_account_status("ACC102")

print("KYC Complete using Nested Unpacking:", kyc_complete)