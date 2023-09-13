# Your task is to remove all duplicate words from a string, leaving only single (first) words entries.
#
# Example:
#
# Input:
#
# 'alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'
#
# Output:
#
# 'alpha beta gamma delta'


# MY SOLUTION

def remove_duplicate_words(s):
    final_arr = []
    for i in s.split():
        if i not in final_arr:
            final_arr.append(i)
    final_str = ' '.join(i for i in final_arr)
    return final_str


# DEMONSTRATION

print(remove_duplicate_words("alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta"))
print(remove_duplicate_words("my cat is my cat fat"))
