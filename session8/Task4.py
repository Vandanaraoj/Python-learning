from functools import reduce


def aggregate_tokens(tokens):
    """
    Calculate cumulative product using reduce().

    LEGB:
    tokens is a Local variable.
    product and token are Local variables of the
    reduce operation.
    limit is a Local variable of this function.
    """

    limit = 1000000

    def multiply(product, token):
        if product * token > limit:
            return token

        return product * token

    result = reduce(multiply, tokens)

    return result


print("\n========== TASK 4 ==========")

tokens = [10, 100, 5, 200, 2]

print("Security Tokens:", tokens)

master_hash = aggregate_tokens(tokens)

print("Master Hash:", master_hash)