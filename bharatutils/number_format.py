
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
