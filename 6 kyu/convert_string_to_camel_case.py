# Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word
# within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also
# often referred to as Pascal case). The next words should be always capitalized.
#
# Examples
# "the-stealth-warrior" gets converted to "theStealthWarrior"
#
# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"
#
# "The_Stealth-Warrior" gets converted to "TheStealthWarrior"


# MY SOLUTION

def to_camel_case(text):
    new_text = text.replace("_", " ")
    new_text = new_text.replace("-", " ")
    new_text = new_text.split()
    final_str = ""
    for word in new_text:
        if word == new_text[0]:
            final_str += word
        else:
            final_str += word.title()
    return final_str


# DEMONSTRATION

print(to_camel_case("the_stealth_warrior"))

