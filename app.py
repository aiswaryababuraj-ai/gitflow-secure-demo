def add_tax(amount, tax_rate):
    if amount < 0 or tax_rate < 0:
        raise ValueError("amount and tax_rate must be non-negative")
    return amount + (amount * tax_rate)