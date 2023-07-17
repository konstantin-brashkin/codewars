# There is an array of strings. All strings contains similar letters except one. Try to find it!
#
# find_uniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]) # => 'BbBb' find_uniq([ 'abc', 'acb', 'bac',
# 'foo', 'bca', 'cab', 'cba' ]) # => 'foo' Strings may contain spaces. Spaces are not significant, only non-spaces
# symbols matters. E.g. string that contains only spaces is like empty string.
#
# It’s guaranteed that array contains more than 2 strings.


# MY SOLUTION

def find_uniq(arr):
    one_symbols = arr[0].lower()
    if (len(arr[0]) == 1) and (arr[0] != arr[1]) and (arr[0] != arr[2]):
        return arr[0]
    two_symbols = ""
    for element in arr:
        for i in element.lower():
            if i not in one_symbols:
                two_symbols += i
    for element in arr:
        for i in element.lower():
            if i in two_symbols:
                return element


# DEMONSTRATION

print(find_uniq(['abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba']))

