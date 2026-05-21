def normalize_to_usd(amount, currency_code, fx_rates):
    """Normalizes local currency amounts to USD using a provided FX rate dictionary."""
    # fx_rates example: {'NGN': 1500, 'GHS': 14.5, 'KES': 130}
    rate = fx_rates.get(currency_code.upper())
    if not rate or rate == 0: return amount
    return round(amount / rate, 2)