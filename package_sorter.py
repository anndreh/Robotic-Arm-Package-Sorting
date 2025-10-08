# RULES
# bulky: >= 1.000.000 or >= 150
# heavy: >= 20

# DISPATCH
# standard: not bulky and not heavy
# special: (bulky or heavy) BUT not both
# rejected: bulky and heavy

def sort(width, height, length, mass):

    is_heavy = (mass >= 20)
    is_bucky = (width * height * length >= 1000000 or
                width >= 150 or
                height >= 150 or
                length >= 150)

    if is_bucky and is_heavy:
        return "REJECTED"
    elif is_bucky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"
