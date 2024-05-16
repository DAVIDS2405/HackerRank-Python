
def missingCharacters(s):
    all_digits = set('0123456789')
    all_letters = set('abcdefghijklmnopqrstuvwxyz')

    to_lower = str(s).lower()

    missing_digits = sorted(all_digits - to_lower)
    missing_letters = sorted(all_letters - to_lower)

    result = ''.join(missing_digits + missing_letters)

    return result
