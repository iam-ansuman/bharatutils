from datetime import date

FIXED_FESTIVALS = {
    "New Year":          (1, 1),
    "Republic Day":      (1, 26),
    "Independence Day":  (8, 15),
    "Gandhi Jayanti":    (10, 2),
    "Christmas":         (12, 25),
}

# Verified against official Government of India holiday lists
# and Drik Panchang (2027)
MOVABLE_FESTIVALS = {
    2023: {
        "Makar Sankranti":    (1, 15),
        "Holi":               (3, 8),
        "Ram Navami":         (3, 30),
        "Mahavir Jayanti":    (4, 4),
        "Good Friday":        (4, 7),
        "Eid ul-Fitr":        (4, 22),
        "Buddha Purnima":     (5, 5),
        "Eid ul-Adha":        (6, 29),
        "Muharram":           (7, 29),
        "Raksha Bandhan":     (8, 30),
        "Janmashtami":        (9, 7),
        "Ganesh Chaturthi":   (9, 19),
        "Milad-un-Nabi":      (9, 28),
        "Dussehra":           (10, 24),
        "Diwali":             (11, 12),
        "Guru Nanak Jayanti": (11, 27),
    },
    2024: {
        "Makar Sankranti":    (1, 15),
        "Holi":               (3, 25),
        "Good Friday":        (3, 29),
        "Eid ul-Fitr":        (4, 11),
        "Ram Navami":         (4, 17),
        "Mahavir Jayanti":    (4, 21),
        "Buddha Purnima":     (5, 23),
        "Eid ul-Adha":        (6, 17),
        "Muharram":           (7, 17),
        "Raksha Bandhan":     (8, 19),
        "Janmashtami":        (8, 26),
        "Ganesh Chaturthi":   (9, 7),
        "Milad-un-Nabi":      (9, 16),
        "Dussehra":           (10, 12),
        "Diwali":             (10, 31),
        "Guru Nanak Jayanti": (11, 15),
    },
    2025: {
        "Makar Sankranti":    (1, 14),
        "Holi":               (3, 14),
        "Eid ul-Fitr":        (3, 31),
        "Ram Navami":         (4, 6),
        "Mahavir Jayanti":    (4, 10),
        "Good Friday":        (4, 18),
        "Buddha Purnima":     (5, 12),
        "Eid ul-Adha":        (6, 7),
        "Muharram":           (7, 6),
        "Raksha Bandhan":     (8, 9),
        "Janmashtami":        (8, 16),
        "Ganesh Chaturthi":   (8, 27),
        "Milad-un-Nabi":      (9, 5),
        "Dussehra":           (10, 2),
        "Diwali":             (10, 20),
        "Guru Nanak Jayanti": (11, 5),
    },
    2026: {
        "Makar Sankranti":    (1, 14),
        "Holi":               (3, 4),
        "Eid ul-Fitr":        (3, 21),
        "Ram Navami":         (3, 26),
        "Mahavir Jayanti":    (3, 31),
        "Good Friday":        (4, 3),
        "Buddha Purnima":     (5, 1),
        "Eid ul-Adha":        (5, 27),
        "Muharram":           (6, 26),
        "Milad-un-Nabi":      (8, 26),
        "Janmashtami":        (9, 4),
        "Ganesh Chaturthi":   (9, 14),
        "Dussehra":           (10, 20),
        "Diwali":             (11, 8),
        "Guru Nanak Jayanti": (11, 24),
    },
    2027: {
        "Makar Sankranti":    (1, 15),
        "Eid ul-Fitr":        (3, 10),
        "Holi":               (3, 22),
        "Good Friday":        (3, 26),
        "Ram Navami":         (4, 15),
        "Buddha Purnima":     (5, 20),
        "Eid ul-Adha":        (5, 17),
        "Muharram":           (6, 16),
        "Raksha Bandhan":     (8, 17),
        "Janmashtami":        (8, 25),
        "Ganesh Chaturthi":   (9, 4),
        "Dussehra":           (10, 9),
        "Diwali":             (10, 29),
        "Guru Nanak Jayanti": (11, 14),
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
