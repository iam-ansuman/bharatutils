
import re

PAN_PATTERN = re.compile(r"^[A-Z]{5}[0-9]{4}[A-Z]{1}$")

HOLDER_TYPES = {
    "P": "Individual",
    "C": "Company",
    "H": "Hindu Undivided Family",
    "F": "Firm / Partnership",
    "T": "Trust",
    "G": "Government",
    "A": "Association of Persons",
    "B": "Body of Individuals",
    "L": "Local Authority",
    "J": "Artificial Juridical Person",
}


def validate_pan(pan):
    """Check if a PAN is valid. Returns True or False."""
    if pan is None or not isinstance(pan, str):
        return False
    pan = pan.strip().upper()
    if len(pan) != 10 or not PAN_PATTERN.match(pan):
        return False
    return pan[3] in HOLDER_TYPES


def parse_pan(pan):
    """Extract holder type and name initial from a PAN."""
    if not validate_pan(pan):
        return None
    pan = pan.strip().upper()
    return {
        "pan": pan,
        "holder_type": HOLDER_TYPES[pan[3]],
        "name_initial": pan[4],
        "is_individual": pan[3] == "P",
    }
