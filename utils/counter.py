from functools import reduce
def count_words(sentence):
    '''Counts number of words in sentence
    
    Args:
        sentence: target sentence to be processed
    Returns:
        Dictionary of words and number of times it occurred in sentence
    '''
    
    normalized_doc = ''.join(c.lower()
                                  if c.isalpha()
                                  else ' ' for c in sentence)
    frequencies = {}
    for word in normalized_doc.split():
        frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies

def combine_counts(d1, d2):
    '''Combines two dictionaries in one.
    Each processed sentence data stored in dictionary.
    This function combines two dictionaries with correct
    number of words occurred.
    
    Args:
        d1: first dictionary
        d2: second dictionary
    Result:
        Combined dictionary that contains sum of words
        and number of times they occurred
    '''

    d = d1.copy()
    for word, count in d2.items():
        d[word] = d.get(word, 0) + count
    return d