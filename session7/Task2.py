# Task - 2
def execute_bulk_transfer(sender_account, *amounts):
    """Process multiple transfers from a starting balance of 10,000.

    Args:
        sender_account (str): Account initiating the transfers.
        *amounts (float): Transfer amounts to subtract from the balance.

    Returns:
        float: Remaining balance after all transfers.

    Raises:
        ValueError: If a transfer amount is negative.
    """
    balance = 10000.0

    for amount in amounts:
        if amount < 0:
            raise ValueError("Transfer amount cannot be negative.")

        balance -= amount
        print(
            f"Ledger: {sender_account} transferred "
            f"{amount:.2f}; balance = {balance:.2f}"
        )

    return balance

print(execute_bulk_transfer("ACC101", 1000, 2000, 500))
print(execute_bulk_transfer("ACC102"))
print(execute_bulk_transfer("ACC103", 0))