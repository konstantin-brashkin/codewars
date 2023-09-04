# Assume "#" is like a backspace in string. This means that string "a#bc#d" actually is "bd"
#
# Your task is to process a string with "#" symbols.
#
# Examples
# "abc#d##c"      ==>  "ac"
# "abc##d######"  ==>  ""
# "#######"       ==>  ""
# ""              ==>  ""


# MY SOLUTION

def clean_string(s):
    result = []
    for c in s:
        if c == '#':
            if result:
                result.pop()
        else:
            result.append(c)
    return ''.join(result)


# DEMONSTRATION

print(clean_string('abc#d##c'))
print(clean_string('abc####d##c#'))
print(clean_string("#######a"))
print(clean_string("C03}ve##C####Z"))
