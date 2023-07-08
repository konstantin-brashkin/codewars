# This time no story, no theory. The examples below show you how to write function accum:
#
# Examples:
# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"
# The parameter of accum is a string which includes only letters from a..z and A..Z.


# MY SOLUTION

def accum(s):
    final_str = ''
    counter = 0
    for letter in s.lower():
        final_str += (letter.upper() + (letter * counter))
        final_str += '-'
        counter += 1
    return final_str[:-1]


# DEMONSTRATION

print(accum('abcd'))
print(accum("NyffsGeyylB"))
