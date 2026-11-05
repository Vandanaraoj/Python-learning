def calculate_compound_interest(
        principal,
        annual_rate,
        years,
        compounds_per_year):

    """
    Calculate compound interest.

    Args:
        principal (float): Initial investment amount.
        annual_rate (float): Annual interest rate.
        years (int): Number of years.
        compounds_per_year (int): Number of times interest is compounded.

    Returns:
        float: Final amount after compound interest.

    Raises:
        ValueError: If the interest rate is negative.
    """

    if annual_rate < 0:
        raise ValueError("Interest rate cannot be negative")

    amount = principal * (
        1 + annual_rate / compounds_per_year
    ) ** (compounds_per_year * years)

    return amount


print("\n--- Task 6: Compound Interest ---")

compound_amount = calculate_compound_interest(
    10000,
    0.05,
    2,
    1
)

print("Final Compound Amount:", compound_amount)