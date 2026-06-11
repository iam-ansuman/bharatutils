# bharatutils 🇮🇳

Python utilities for Indian developers — because `1,500,000` should display as `₹15 L`.

Lakh/crore formatting · GST & PAN validation · Address parsing · Festival calendar

## Why?

Every Indian developer has written these same utility functions a hundred times:

```python
# Without bharatutils 😩
df["salary_display"] = df["salary"].apply(
    lambda x: f"₹{round(x/100000, 2)} L" if x >= 100000 else f"₹{x:,}"
)  # ...and it crashes on NaN

# With bharatutils 😎
from bharatutils import format_inr
df["salary_display"] = df["salary"].apply(format_inr)   # handles NaN, strings, negatives
```

## Install

```bash
pip install bharatutils
```

## Features

### 💰 Indian number formatting
```python
from bharatutils import format_inr, to_lakh, to_crore

format_inr(1500000)     # '₹15.0 L'
format_inr(50000000)    # '₹5.0 Cr'
format_inr("15,00,000") # '₹15.0 L'  — handles messy strings
to_lakh(1500000)        # 15.0
```

### 🧾 GST validation — with real checksum
```python
from bharatutils import validate_gstin_strict, parse_gstin

validate_gstin_strict("27AAAPZ2318J1ZI")  # True — verifies the check digit
parse_gstin("27AAAPZ2318J1ZI")
# {'state': 'Maharashtra', 'pan': 'AAAPZ2318J', 'entity_number': '1', ...}
```
Catches single-character typos that format-only validators miss.

### 🪪 PAN validation + holder type
```python
from bharatutils import parse_pan

parse_pan("AAAPZ2318J")
# {'holder_type': 'Individual', 'is_individual': True, ...}
# P=Person, C=Company, T=Trust, G=Government...
```

### 📍 Indian address parsing
```python
from bharatutils import parse_address

parse_address("Flat 302, Nr. SBI ATM, MG Road, Pune - 411001")
# {'pincode': '411001', 'state': 'Maharashtra', 'city': 'Pune'}
```
Handles space-broken pincodes ("700 016"), ignores phone numbers, never crashes.

### 🪔 Festival calendar
```python
from bharatutils import next_festival, days_until

next_festival()        # {'name': 'Muharram', 'date': datetime.date(2026, 6, 26)}
days_until("Diwali")   # 150
```
Covers Hindu, Muslim, Christian, Sikh & Jain festivals plus national holidays — verified against official Government of India lists.

## Status

`v0.1.0` — early but tested. Pincode→state mapping is prefix-based (~95% accurate); exact-lookup coming in v0.2.

Found a bug? [Open an issue](../../issues) — responses are fast.

## License

MIT
