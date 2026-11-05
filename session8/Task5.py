def sensitivity_boost(data):
    """
    Multiply all values by 1.5.

    LEGB:
    data is a Local variable.
    value is Local to the lambda function.
    """

    return list(
        map(
            lambda value: value * 1.5,
            data
        )
    )


def noise_reduction(data):
    """
    Remove values below 100.

    LEGB:
    data is a Local variable.
    value is Local to the lambda function.
    """

    return list(
        filter(
            lambda value: value >= 100,
            data
        )
    )


def security_engine(data_stream, strategy):
    """
    Apply a security strategy to the data stream.

    LEGB:
    data_stream and strategy are Local variables.
    The strategy function is received from the caller.
    """

    boosted_data = sensitivity_boost(data_stream)

    print("After Sensitivity Boost:", boosted_data)

    result = strategy(boosted_data)

    return result


print("\n========== TASK 5 ==========")

raw_stream = [50, 80, 120, 200]

print("Original Data:", raw_stream)

final_result = security_engine(
    raw_stream,
    noise_reduction
)

print("Final Result:", final_result)