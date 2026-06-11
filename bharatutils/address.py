
import re

PINCODE_PATTERN = re.compile(r"\b[1-9][0-9]{5}\b")

PINCODE_PREFIX_TO_STATE = {
    "11": "Delhi",
    "12": "Haryana", "13": "Haryana",
    "14": "Punjab", "15": "Punjab",
    "16": "Chandigarh",
    "17": "Himachal Pradesh",
    "18": "Jammu & Kashmir", "19": "Jammu & Kashmir",
    "20": "Uttar Pradesh", "21": "Uttar Pradesh", "22": "Uttar Pradesh",
    "23": "Uttar Pradesh", "24": "Uttar Pradesh", "25": "Uttar Pradesh",
    "26": "Uttar Pradesh", "27": "Uttar Pradesh", "28": "Uttar Pradesh",
    "30": "Rajasthan", "31": "Rajasthan", "32": "Rajasthan", "33": "Rajasthan", "34": "Rajasthan",
    "36": "Gujarat", "37": "Gujarat", "38": "Gujarat", "39": "Gujarat",
    "40": "Maharashtra", "41": "Maharashtra", "42": "Maharashtra",
    "43": "Maharashtra", "44": "Maharashtra",
    "45": "Madhya Pradesh", "46": "Madhya Pradesh", "47": "Madhya Pradesh", "48": "Madhya Pradesh",
    "49": "Chhattisgarh",
    "50": "Telangana",
    "51": "Andhra Pradesh", "52": "Andhra Pradesh", "53": "Andhra Pradesh",
    "56": "Karnataka", "57": "Karnataka", "58": "Karnataka", "59": "Karnataka",
    "60": "Tamil Nadu", "61": "Tamil Nadu", "62": "Tamil Nadu", "63": "Tamil Nadu", "64": "Tamil Nadu",
    "67": "Kerala", "68": "Kerala", "69": "Kerala",
    "70": "West Bengal", "71": "West Bengal", "72": "West Bengal", "73": "West Bengal", "74": "West Bengal",
    "75": "Odisha", "76": "Odisha", "77": "Odisha",
    "78": "Assam",
    "79": "North East",
    "80": "Bihar", "81": "Bihar", "82": "Bihar", "83": "Bihar", "84": "Bihar", "85": "Bihar",
    "90": "Army Postal Service", "91": "Army Postal Service", "92": "Army Postal Service",
    "99": "Army Postal Service",
}

KNOWN_CITIES = [
    "Mumbai", "Delhi", "Bangalore", "Bengaluru", "Hyderabad", "Chennai",
    "Kolkata", "Pune", "Ahmedabad", "Jaipur", "Surat", "Lucknow",
    "Kanpur", "Nagpur", "Indore", "Bhopal", "Patna", "Vadodara",
    "Ludhiana", "Agra", "Nashik", "Varanasi", "Amritsar", "Noida",
    "Gurgaon", "Gurugram", "Chandigarh", "Coimbatore", "Kochi", "Goa",
    "Visakhapatnam", "Thane", "Guwahati", "Bhubaneswar", "Mysore", "Mysuru",
]


def extract_pincode(address):
    """Find the pincode in a messy address string. None if not found."""
    if address is None or not isinstance(address, str):
        return None
    cleaned = re.sub(r"(\b[1-9][0-9]{2})\s+([0-9]{3}\b)", r"\1\2", address)
    match = PINCODE_PATTERN.search(cleaned)
    return match.group() if match else None


def pincode_to_state(pincode):
    """Get the state from a pincode. None if unknown."""
    if pincode is None:
        return None
    pincode = str(pincode).strip()
    if not re.match(r"^[1-9][0-9]{5}$", pincode):
        return None
    return PINCODE_PREFIX_TO_STATE.get(pincode[:2])


def parse_address(address):
    """Parse a messy Indian address. Always returns a dict."""
    result = {"raw": address, "pincode": None, "state": None, "city": None}
    if address is None or not isinstance(address, str):
        return result
    result["pincode"] = extract_pincode(address)
    if result["pincode"]:
        result["state"] = pincode_to_state(result["pincode"])
    address_lower = address.lower()
    for city in KNOWN_CITIES:
        if re.search(r"\b" + city.lower() + r"\b", address_lower):
            result["city"] = city
            break
    return result
