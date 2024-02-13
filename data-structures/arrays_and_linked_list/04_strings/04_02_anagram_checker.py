"""
Anagrams:
The goal of this exercise is to write some code to determine if two strings
are anagrams of each other.

An anagram is a word (or phrase) that is formed by rearranging the letters of
another word (or phrase).

For example:

"rat" is an anagram of "art"
"alert" is an anagram of "alter"
"Slot machines" is an anagram of "Cash lost in me"
Your function should take two strings as input and return True if the two
words are anagrams and False if they are not.

You can assume the following about the input strings:

No punctuation
No numbers
No special characters

"""

# replace => O(nlogn)
# for loop => O(n*(2 + nlogn)) => O(n^2logn)
# O(n^2logn)
def anagram_checker(w1, w2):
    """return if w1 and w2 are anagram"""
    _w1 = w1.replace(" ", "")
    _w2 = w2.replace(" ", "")
    print(_w2)
    
    if len (_w1) != len(_w2):
        return False
    for letter in _w1:
        if not letter in _w2:
            return False
        _w2 = _w2.replace(letter, '', 1)
    return len(_w2) == 0
    
### REVIEW - anagram_checker (CHATGPT)
# Efficiency: This approach is relatively efficient for short strings, but it may not be optimal for very long strings due to the repeated use of str.replace() inside the loop, which creates a new string each time it's called.
# Readability: The code is straightforward and easy to understand. However, the debugging print statement (print(_w2)) could be removed for clarity in the final version.
# Functionality: The code correctly identifies anagrams by ensuring that each letter in _w1 has a corresponding letter in _w2 and vice versa.

# 2*replace => O(n)
# for loop (w2) => O(4n)=> O(n)
# for loop (W1) => O(4m) => O(m)
# if => O(2) => O(1)
# for loop (_w2) => O(4j) => O(j) => O(j)
# Complexity => O(n) + O(n) + O(n) => O(n)
def anagram_checker_with_dict(w1, w2):
    """return if w1 and w2 are anagram"""
    _w1 = {}
    _w2 = {}
    w1 = w1.replace(" ", "")
    w2 = w2.replace(" ", "")
    for letter in w2:
        if letter in _w2:
            _w2[letter] +=1
        else:
            _w2[letter] = 1
    for letter in w1:
        if letter in _w1:
            _w1[letter] +=1
        else:
            _w1[letter] = 1
    if len(_w2.keys()) != len(_w2.keys()):
        return False
    for key in _w1:
        if not key in _w2:
            return False
        if _w1[key] != _w2[key]:
            return False
    return True

# using sorted python builtin method
# complexity
# replace => O(n)
# sorted => O(n logn)
## complexity => O(nlogn)
def anagram_checker_sort(w1, w2):
    """return if w1 and w2 are anagram"""
    _w1 = sorted(w1.replace(" ", ""))
    _w2 = sorted(w2.replace(" ", ""))
    
    return _w1 == _w2

# Test Cases
print("Anagram Check:")
print("Anagram Check with dictionary:")
print(anagram_checker('boom', 'moot'))
print(anagram_checker('anagram', 'nag a ram'))
print(anagram_checker_with_dict('slot machines', 'cash lost in me'))