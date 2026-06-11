
from datetime import date

FIXED_FESTIVALS = {
    "New Year":          (1, 1),
    "Republic Day":      (1, 26),
    "Independence Day":  (8, 15),
    "Gandhi Jayanti":    (10, 2),
    "Christmas":         (12, 25),
}

# Verified against official Government of India holiday lists
MOVABLE_FESTIVALS = {
    2026: {
        "Makar Sankranti":    (1, 14),
        "Holi":               (3, 4),
        "Eid ul-Fitr":        (3, 21),
        "Ram Navami":         (3, 26),
        "Mahavir Jayanti":    (3, 31),
        "Good Friday":        (4, 3),
        "Eid ul-Adha":        (5, 27),
        "Muharram":           (6, 26),
        "Milad-un-Nabi":      (8, 26),
        "Janmashtami":        (9, 4),
        "Ganesh Chaturthi":   (9, 14),
        "Dussehra":           (10, 20),
        "Diwali":             (11, 8),
        "Guru Nanak Jayanti": (11, 24),
    },
}


def get_festivals(year):
    """All festivals for a year, sorted by date."""
    festivals = []
    for name, (m, d) in FIXED_FESTIVALS.items():
        festivals.append({"name": name, "date": date(year, m, d), "type": "fixed"})
    if year in MOVABLE_FESTIVALS:
        for name, (m, d) in MOVABLE_FESTIVALS[year].items():
            festivals.append({"name": name, "date": date(year, m, d), "type": "movable"})
    festivals.sort(key=lambda f: f["date"])
    return festivals


def next_festival(from_date=None):
    """The next upcoming festival from a given date (default: today)."""
    if from_date is None:
        from_date = date.today()
    for year in [from_date.year, from_date.year + 1]:
        for f in get_festivals(year):
            if f["date"] >= from_date:
                return f
    return None


def days_until(festival_name, from_date=None):
    """Days remaining until a festival. None if not found."""
    if from_date is None:
        from_date = date.today()
    for year in [from_date.year, from_date.year + 1]:
        for f in get_festivals(year):
            if f["name"].lower() == festival_name.lower() and f["date"] >= from_date:
                return (f["date"] - from_date).days
    return None


def is_festival(check_date=None):
    """Is this date a festival? Returns the festival name or None."""
    if check_date is None:
        check_date = date.today()
    for f in get_festivals(check_date.year):
        if f["date"] == check_date:
            return f["name"]
    return None
