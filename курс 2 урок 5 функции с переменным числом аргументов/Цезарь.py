def alphabet(shift):
    shift = shift % len(lower_cyrillic)
    return lower_cyrillic[shift:] + \
           lower_cyrillic[:shift] + \
           upper_cyrillic[shift:] + \
           upper_cyrillic[:shift]