import unicodedata


def remove_accents(word: str) -> str:
    word_nfd = unicodedata.normalize('NFD', word)
    word_without_accent = ''.join([char for char in word_nfd if unicodedata.category(char) != 'Mn'])
    return word_without_accent
