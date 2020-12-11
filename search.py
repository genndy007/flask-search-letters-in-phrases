# my function to deploy at the web - it searches for letters in a given phrase
def search4letters(phrase: str, letters: str='aeiou') -> set:
    '''Returns set of letters found in phrase'''
    return set(letters).intersection(set(phrase))