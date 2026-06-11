
import re

STATE_CODES = {
    "01": "Jammu & Kashmir",  "02": "Himachal Pradesh",
    "03": "Punjab",           "04": "Chandigarh",
    "05": "Uttarakhand",      "06": "Haryana",
    "07": "Delhi",            "08": "Rajasthan",
    "09": "Uttar Pradesh",    "10": "Bihar",
    "11": "Sikkim",           "12": "Arunachal Pradesh",
    "13": "Nagaland",         "14": "Manipur",
    "15": "Mizoram",          "16": "Tripura",
    "17": "Meghalaya",        "18": "Assam",
    "19": "West Bengal",      "20": "Jharkhand",
    "21": "Odisha",           "22": "Chhattisgarh",
    "23": "Madhya Pradesh",   "24": "Gujarat",
    "25": "Daman & Diu",      "26": "Dadra & Nagar Haveli",
    "27": "Maharashtra",      "28": "Andhra Pradesh",
    "29": "Karnataka",        "30": "Goa",
    "31": "Lakshadweep",      "32": "Kerala",
    "33": "Tamil Nadu",       "34": "Puducherry",
    "35": "Andaman & Nicobar","36": "Telangana",
    "37": "Andhra Pradesh (New)",
}

GSTIN_PATTERN = re.compile(r"^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{1}[1-9A-Z]{1}Z[0-9A-Z]{1}$")


def validate_gstin(gstin):
    """Check if a GSTIN has valid format and a real state code."""
    if gstin is None or not isinstance(gstin, str):
        return False
    gstin = gstin.strip().upper()
    if len(gstin) != 15 or not GSTIN_PATTERN.match(gstin):
        return False
    return gstin[:2] in STATE_CODES


def parse_gstin(gstin):
    """Break a GSTIN into state, PAN, entity number. None if invalid."""
    if not validate_gstin(gstin):
        return None
    gstin = gstin.strip().upper()
    return {
        "gstin": gstin,
        "state_code": gstin[:2],
        "state": STATE_CODES[gstin[:2]],
        "pan": gstin[2:12],
        "entity_number": gstin[12],
        "check_digit": gstin[14],
    }


def gstin_check_digit(gstin_first_14):
    """Official mod-36 checksum for GSTIN."""
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    total = 0
    for i, char in enumerate(gstin_first_14):
        value = chars.index(char)
        factor = 2 if i % 2 != 0 else 1
        product = value * factor
        total += product // 36 + product % 36
    return chars[(36 - total % 36) % 36]


def validate_gstin_strict(gstin):
    """Full validation: format + state + checksum."""
    if not validate_gstin(gstin):
        return False
    gstin = gstin.strip().upper()
    return gstin_check_digit(gstin[:14]) == gstin[14]
