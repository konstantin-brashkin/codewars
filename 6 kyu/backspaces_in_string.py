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
    s_split = list(s)

    while True:
        if "#" in s_split:
            hashtag_index = s_split.index("#")
            if hashtag_index != 0:
                del s_split[hashtag_index - 1]
                s_split.remove("#")
            else:
                s_split.remove("#")
        else:
            break

    final_str = "".join(i for i in s_split)
    return final_str


# DEMONSTRATION

print(clean_string('abc#d##c'))
print(clean_string('abc####d##c#'))
print(clean_string("#######a"))
print(clean_string("C03}ve##C####Z"))
