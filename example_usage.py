"""
example_usage.py -- Demonstrates SalesTaxExemptClient
"""
from client import SalesTaxExemptClient

def main():
    client = SalesTaxExemptClient()
    result = client.check_exempt(state_code="NY", product_category="clothing")
    print("[Tax Exemption Status Result]")
    print(f"Exempt: {result['is_exempt']}")
    print(f"Notes: {result['notes']}")

if __name__ == "__main__":
    main()
