def to_lakh(number):
    """Convert a number to lakhs. Handles strings, negatives, None, NaN."""
    if number is None or (isinstance(number, float) and number != number):
        return None
    if isinstance(number, str):
        number = float(number.replace(",", "").replace("₹", "").strip())
    return round(number / 100_000, 2)


def to_crore(number):
    """Convert a number to crores. Handles strings, negatives, None, NaN."""
    if number is None or (isinstance(number, float) and number != number):
        return None
    if isinstance(number, str):
        number = float(number.replace(",", "").replace("₹", "").strip())
    return round(number / 10_000_000, 2)


def format_inr(number, symbol=True):
    """
    Format a number in Indian style (lakh/crore).
    symbol=False gives you 15.0 L without the rupee sign.
    """
    if number is None or (isinstance(number, float) and number != number):
        return "N/A"
    if isinstance(number, str):
        number = float(number.replace(",", "").replace("₹", "").strip())
    prefix = "₹" if symbol else ""
    negative = number < 0
    number = abs(number)
    if number >= 10_000_000:
        result = f"{prefix}{to_crore(number)} Cr"
    elif number >= 100_000:
        result = f"{prefix}{to_lakh(number)} L"
    else:
        result = f"{prefix}{number:,.0f}"
    return f"-{result}" if negative else result


def indian_commas(number):
    """
    Format with Indian-style comma grouping: 1500000 -> '15,00,000'.
    Last 3 digits grouped, then every 2. Handles strings, negatives, None, NaN.
    """
    if number is None or (isinstance(number, float) and number != number):
        return None
    if isinstance(number, str):
        number = float(number.replace(",", "").replace("₹", "").strip())
    negative = number < 0
    number = abs(number)
    whole = str(int(number))
    if len(whole) > 3:
        last3 = whole[-3:]
        rest = whole[:-3]
        groups = []
        while len(rest) > 2:
            groups.insert(0, rest[-2:])
            rest = rest[:-2]
        if rest:
            groups.insert(0, rest)
        whole = ",".join(groups) + "," + last3
    return f"-{whole}" if negative else whole
