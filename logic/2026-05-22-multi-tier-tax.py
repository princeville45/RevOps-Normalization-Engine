def calculate_jurisdiction_tax(amount, region_code):
    """Calculates multi-tier sales tax for EMEA regions (e.g., Nigeria, Kenya, SA)."""
    tax_config = {
        'NG': {'vat': 0.075, 'levy': 0.01},
        'KE': {'vat': 0.16, 'levy': 0.02},
        'ZA': {'vat': 0.15, 'levy': 0.00}
    }
    
    config = tax_config.get(region_code.upper(), {'vat': 0.0, 'levy': 0.0})
    total_tax = amount * (config['vat'] + config['levy'])
    return round(total_tax, 2)