# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks
# untouched.
#
# Examples
# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !


# MY SOLUTION

import string


def pig_it(text):
    word_list = text.split()
    final_str = ''
    punctuation_symbols = [',', '!', '?', '.']
    for element in word_list:
        if element not in punctuation_symbols:
            final_str += element[1:] + element[0] + "ay" " "
        else:
            final_str += element
    return final_str.rstrip()


# DEMONSTRATION

print(pig_it('This is my string !'))
