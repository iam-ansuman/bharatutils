<div align="center">

# 🇮🇳 bharatutils

### Python utilities for Indian developers — because `1,500,000` should display as `₹15 L`

![PyPI](https://img.shields.io/pypi/v/bharatutils?color=ff9933&label=PyPI)
![Python](https://img.shields.io/pypi/pyversions/bharatutils?color=138808)
![License](https://img.shields.io/github/license/iam-ansuman/bharatutils?color=000080)
![Downloads](https://img.shields.io/pypi/dm/bharatutils?color=ff9933)

**Lakh/crore formatting · GST & PAN validation · Address parsing · Festival calendar**

Zero dependencies. Never crashes on messy data. Made for Bharat. 

```bash
pip install bharatutils
```

</div>

---

## 😩 The problem every Indian developer knows

```python
# Without bharatutils — written for the 100th time, breaks on NaN
df["salary_display"] = df["salary"].apply(
    lambda x: f"₹{round(x/100000, 2)} L" if x >= 100000 else f"₹{x:,}"
)

# With bharatutils — one import, handles everything
from bharatutils import format_inr
df["salary_display"] = df["salary"].apply(format_inr)
```

Western libraries format millions and billions, validate US Social Security numbers,
and know when Thanksgiving falls. **bharatutils** speaks lakh and crore, validates
GSTIN with real checksums, reads addresses with landmarks instead of street numbers,
and knows when Diwali is.

---

## ✨ Features

### 💰 Indian number formatting

```python
from bharatutils import format_inr, to_lakh, to_crore

format_inr(1500000)        # '₹15.0 L'
format_inr(50000000)       # '₹5.0 Cr'
format_inr("15,00,000")    # '₹15.0 L'   — messy strings? handled
format_inr(-750000)        # '-₹7.5 L'   — negatives? handled
format_inr(float("nan"))   # 'N/A'       — pandas NaN? handled
indian_commas(15000000)    # '1,50,00,000' — full Indian grouping
```

Drop it straight into a pandas pipeline on 100,000 dirty rows. It won't flinch.

### 🧾 GST validation — with the real checksum

```python
from bharatutils import validate_gstin_strict, parse_gstin

validate_gstin_strict("27AAAPZ2318J1ZI")   # True — verifies check digit
validate_gstin_strict("27AAAPZ2319J1ZI")   # False — catches the typo!

parse_gstin("27AAAPZ2318J1ZI")
# {'state': 'Maharashtra', 'pan': 'AAAPZ2318J', 'entity_number': '1', ...}
```

Most validators only check the format pattern. bharatutils implements the
**official mod-36 check-digit algorithm** — a single wrong character fails validation,
exactly as it should.

### 🪪 PAN validation + holder type decoding

```python
from bharatutils import parse_pan

parse_pan("AAAPZ2318J")
# {'holder_type': 'Individual', 'name_initial': 'Z', 'is_individual': True}
```

The 4th character of every PAN hides its meaning: `P` person, `C` company,
`T` trust, `G` government — decoded for you.

### 📍 Indian address parsing

```python
from bharatutils import parse_address

parse_address("Flat 302, Shree Krishna Apts, Nr. SBI ATM, MG Road, Pune - 411001")
# {'pincode': '411001', 'state': 'Maharashtra', 'city': 'Pune'}
```

Landmarks, flat numbers, "Nr. SBI ATM" — none of it confuses the parser.
Space-broken pincodes (`700 016`) get normalized. Phone numbers don't fool it.
It **always** returns a dict, never crashes.

### 🪔 One calendar for all of Bharat

```python
from bharatutils import get_festivals, next_festival, days_until

next_festival()          # {'name': 'Muharram', 'date': datetime.date(2026, 6, 26)}
days_until("Diwali")     # 150
get_festivals(2026)      # every festival of the year, sorted by date
```

Holi and Eid. Christmas and Guru Nanak Jayanti. Buddha Purnima and Diwali.
**One calendar, every celebration — the way India actually lives.**
Dates for 2023–2027, verified against official Government of India holiday lists.

---

## 📖 Quick reference

| Function | What it does |
|---|---|
| `format_inr(n)` | Smart ₹ formatting (auto lakh/crore) |
| `to_lakh(n)` / `to_crore(n)` | Plain numeric conversion |
| `validate_gstin(g)` | Format + state check |
| `validate_gstin_strict(g)` | Format + state + checksum |
| `parse_gstin(g)` | Extract state, PAN, entity number |
| `validate_pan(p)` / `parse_pan(p)` | PAN check + holder type decode |
| `parse_address(a)` | Pincode, state, city from messy text |
| `extract_pincode(a)` / `pincode_to_state(p)` | The building blocks |
| `get_festivals(year)` | Full year calendar, sorted |
| `next_festival()` / `days_until(name)` / `is_festival(date)` | Calendar queries |

---

## 🗺️ Roadmap

- [x] v0.1 — five core modules, published
- [x] v0.1.2 — festival data 2023–2027, Buddha Purnima added
- [ ] v0.2 — exact pincode→district lookup, pandas accessor (`df["col"].india.to_lakh()`)
- [ ] v0.3 — IFSC validation, vehicle registration parsing, regional festival calendars

Honest note: pincode→state mapping is currently prefix-based (~95% accurate).
Exact lookup is the headline feature of v0.2.

## 🤝 Contributing

Found a bug? Wrong festival date? Missing your state's festivals?
[Open an issue](../../issues) — responses are fast. PRs welcome.

## 📄 License

MIT — use it anywhere, build anything, just keep the name on it.

<div align="center">

**Made with ❤️ for every developer who ever wrote a lakh formatter at 2am**

`pip install bharatutils`

</div>
