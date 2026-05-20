def normalize_emea_tax(amount, country_code, is_business=True):
    """Calculates net amount after VAT/Tax based on EMEA regional regulations."""
    # Simplified VAT rates mapping
    vat_rates = {'UK': 0.20, 'FR': 0.20, 'DE': 0.19, 'NG': 0.075, 'ZA': 0.15}
    rate = vat_rates.get(country_code.upper(), 0.0)
    # Businesses often claim back VAT
    if is_business and country_code.upper() in ['UK', 'FR', 'DE']:
        return round(amount, 2) # Net amount remains for accounting
    return round(amount * (1 + rate), 2)