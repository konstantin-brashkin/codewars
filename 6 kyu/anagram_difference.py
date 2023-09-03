# Given two words, how many letters do you have to remove from them to make them anagrams?
# Example
# First word : c od e w ar s (4 letters removed)
# Second word : ha c k er r a nk (6 letters removed)
# Result : 10
# Hints
# A word is an anagram of another word if they have the same letters (usually in a different order).
# Do not worry about case. All inputs will be lowercase.


# MY SOLUTION

def anagram_difference(w1, w2):
    unique_symbols = list(set(w1) & set(w2))
    similar_symbols = []
    for i in unique_symbols:
        array_ui = [w1.count(i), w2.count(i)]
        similar_symbols += [i] * min(array_ui)

    split_w1 = list(w1)
    split_w2 = list(w2)

    for i in similar_symbols:
        split_w1.remove(i)
        split_w2.remove(i)

    return len(split_w1) + len(split_w2)


# DEMONSTRATION


print(anagram_difference('codewars', 'hackerrank'))
print(anagram_difference('aab', 'aaa'))
print(anagram_difference(['w', 's', 'u', 'b', 'w', 'w', 'f', 'l', 'f', 's', 'm', 's', 'u'],
                         ['f', 'g', 't', 'k', 'f', 'c', 'h', 'f', 't', 'c', 'x', 'm', 'u', 'z', 'v', 'b', 'd', 'p', 'j',
                          'c', 'g', 'u']))
