from collections import Counter

from iso15924 import UNICODE_ISO


def detect_script(text):
    """Return a best guess for the script of the given text string"""
    counts = Counter(UNICODE_ISO.get(ord(c)) for c in text)
    useless = {None, 'Zyyy'}
    for iso in useless:
        del counts[iso]
    total = sum(counts.values())
    def is_common(iso):
        if total == 0: return False
        return counts[iso] / total > 0.1

    if is_common('Hani'):
        if is_common('Hira') or is_common('Kana'):
            return 'Jpan'
        elif is_common('Hant') and counts['Hant'] > counts['Hans']:
            return 'Hant'
        elif is_common('Hans') and counts['Hans'] > counts['Hant']:
            return 'Hans'
        else:
            return 'Hani'

    try:
        return counts.most_common(1)[0][0]
    except IndexError:
        return 'Zyyy'


if __name__ == '__main__':
    import sys
    print(detect_script(sys.stdin.read()))

