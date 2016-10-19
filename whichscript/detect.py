from collections import Counter

from iso15924 import UNICODE_ISO


def detect_script(sentences):
    """Return a best guess for the script of the given sentences"""
    def get_counts(sentence):
        return Counter(UNICODE_ISO.get(ord(c)) for c in sentence)

