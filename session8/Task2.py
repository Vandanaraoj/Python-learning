def decode_payload(payload):
    """
    Decode payload using map() and lambda.

    LEGB:
    payload is a Local variable.
    number is Local to the lambda function.
    """

    decoded = list(
        map(
            lambda number: (
                number * 2
                if number % 2 == 0
                else number + 5
            ),
            payload
        )
    )

    return decoded


print("\n========== TASK 2 ==========")

payload = [10, 15, 20, 25]

print("Original Payload:", payload)

decoded_payload = decode_payload(payload)

print("Decoded Payload:", decoded_payload)