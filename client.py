"""
sales-tax-exempt-checker-skill: Client SDK
Audits catalog product categories against US state sales tax compliance exempt lists.
"""
from __future__ import annotations
from typing import Optional


class SalesTaxExemptClient:
    """
    SDK for sales tax policy auditing.
    """

    def check_exempt(
        self,
        state_code: str,
        product_category: str,
    ) -> dict:
        state = state_code.upper()
        cat = product_category.lower()

        exempt = False
        notes = "Standard sales tax applies."

        # Example policy rule simulation
        if state == "NY":
            if cat in ("clothing", "apparel"):
                exempt = True
                notes = "Clothing items under $110 are exempt from NY state sales tax."
        elif state == "CA":
            if cat in ("groceries", "food"):
                exempt = True
                notes = "Groceries are exempt from CA sales tax."

        return {
            "is_exempt": exempt,
            "notes": notes
        }
