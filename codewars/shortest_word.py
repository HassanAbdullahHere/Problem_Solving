"""Simple, given a string of words, return the length of the shortest word(s)."""

def find_short(s):
    l = float('inf')
    for word in s.split():
        if len(word) < l:
            l = len(word)
    return l
