# my function to deploy at the web
def search4letters(phrase: str, letters: str='aeiou') -> set:
    '''Returns set of letters found in phrase'''
    return set(letters).intersection(set(phrase))