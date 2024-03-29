"""
Reverse the words in sentence:
Given a sentence, reverse each word in the sentence while keeping the order
the same!

"""


def word_flipper(our_string):
    """
    Flip the individual words in a sentence

    Args:
       our_string(string): String with words to flip
    Returns:
       string: String with words flipped
    """
    words = our_string.split()
    sentence = []
    for word in words:
        sentence.append(word[::-1])
    return " ".join(sentence)

# Test Cases
print("Pass" if ('retaw' == word_flipper('water')) else "Fail")
print("Pass" if ('sihT si na elpmaxe' ==
                 word_flipper('This is an example')) else "Fail")
print("Pass" if ('sihT si eno llams pets rof ...' ==
                 word_flipper('This is one small step for ...')) else "Fail")