# Usually when you buy something, you're asked whether your credit card number, phone number or answer to your most
# secret question is still correct. However, since someone could look over your shoulder, you don't want that shown
# on your screen. Instead, we mask it.
#
# Your task is to write a function maskify, which changes all but the last four characters into '#'.


# MY SOLUTION

def maskify(cc):
    final_str = ""
    if len(cc) > 4:
        final_str += ("#" * (len(cc) - 4)) + cc[-4:]
        return final_str
    else:
        return cc


# DEMONSTRATION

print(maskify("4556364607935616"))
print(maskify("123"))

