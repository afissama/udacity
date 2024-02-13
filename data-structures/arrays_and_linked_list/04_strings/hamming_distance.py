"""
Hamming Distance:
In information theory, the Hamming distance between two strings of equal
length is the number of positions at which the corresponding symbols are
different.

Calculate the Hamming distace for the following test cases.

"""

def hamming_distance(stc1, stc2):
    """return the hamming distance"""
    """
    efficency: O(n) => n len of stc1 
    space complexity: O(1)
    """
    d = 0
    if len(stc1) != len(stc2):
        raise Exception("len should be equal")
    for i in range(len(stc1)):
        if stc1[i] != stc2[i]:
            d += 1
    return d

def test():
    print("Hamming distance is {}".format(hamming_distance("dogs", "cats") == 3))
    print("Hamming distance is {}".format(hamming_distance("coconut", "caaons") == 5))

test()