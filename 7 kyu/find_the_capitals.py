# Instructions Write a function that takes a single string (word) as argument. The function must return an ordered
# list containing the indexes of all capital letters in the string.
#
# Example (Input --> Output)
# "CodEWaRs" --> [0,3,4,6]


# MY SOLUTION

def capitals(word):
    final_arr = []
    for i in range(0, len(word)):
        if word[i].isupper():
            final_arr.append(i)
    return final_arr


# DEMONSTRATION

print(capitals('CodEWaRs'))
