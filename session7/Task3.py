# Task - 3
def calculate_net_amount(base_amount, **kwargs):
    """Apply dynamically supplied percentage fees or taxes.

    Each keyword value represents a rate expressed as a decimal.
    For example, vat=0.15 represents a 15 percent fee.

    Args:
        base_amount (float): Original monetary amount.
        **kwargs (float): Tax or fee rates to apply sequentially.

    Returns:
        float: Final amount after all supplied rates are applied.

    Raises:
        ValueError: If base_amount or any rate is negative.
    """
    if base_amount < 0:
        raise ValueError("Base amount cannot be negative.")

    net_amount = base_amount

    for fee_name, rate in kwargs.items():
        if rate < 0:
            raise ValueError(f"{fee_name} rate cannot be negative.")

        net_amount *= 1 - rate

    return net_amount
print(calculate_net_amount(1000))
print(calculate_net_amount(1000, vat=0.15))
print(
    calculate_net_amount(
        1000,
        vat=0.15,
        service_fee=0.05
    )
)