# genpark-sales-tax-exempt-checker-skill

> **GenPark AI Agent Skill** -- US state sales tax exemption compliance auditor.

## Quick Start

```python
from client import SalesTaxExemptClient
client = SalesTaxExemptClient()
res = client.check_exempt("CA", "food")
print(res["is_exempt"])
```
