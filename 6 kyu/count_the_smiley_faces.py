# Given an array (arr) as an argument complete the function countSmileys that should return the total number of
# smiling faces.
#
# Rules for a smiling face:
#
# Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
# A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
# Every smiling face must have a smiling mouth that should be marked with either ) or D
# No additional characters are allowed except for those mentioned.
#
# Valid smiley face examples: :) :D ;-D :~)
# Invalid smiley faces: ;( :> :} :]
#
# Example countSmileys([':)', ';(', ';}', ':-D']);       // should return 2; countSmileys([';D', ':-(', ':-)',
# ';~)']);     // should return 3; countSmileys([';]', ':[', ';*', ':$', ';-D']); // should return 1; Note In case of
# an empty array return 0. You will not be tested with invalid input (input will always be an array). Order of the
# face (eyes, nose, mouth) elements will always be the same.


# MY SOLUTION

def count_smileys(arr):
    first_stack = ':;'
    second_stack = '-~'
    third_stack = ')D'
    final_arr = []
    for element in arr:
        tester = True

        if len(element) == 2:
            if element[0] not in first_stack:
                tester = False
            if element[1] not in third_stack:
                tester = False

        elif len(element) == 3:
            if element[0] not in first_stack:
                tester = False
            if element[1] not in second_stack:
                tester = False
            if element[2] not in third_stack:
                tester = False

        if tester:
            final_arr.append(element)
    return len(final_arr)


# DEMONSTRATION

print(count_smileys([':)',':(',':D',':O',':;']))


