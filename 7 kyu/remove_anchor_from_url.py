# Complete the function/method so that it returns the url with anything after the anchor (#) removed.
#
# Examples
# "www.codewars.com#about" --> "www.codewars.com"
# "www.codewars.com?page=1" -->"www.codewars.com?page=1"


# MY SOLUTION

def remove_url_anchor(url):
    split_url = url.split("#")
    return split_url[0]


# DEMONSTRATION

print(remove_url_anchor("www.codewars.com#about"))
print(remove_url_anchor("www.codewars.com/katas/?page=1#about"))
print(remove_url_anchor("www.codewars.com/katas/"))
