# ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6
# digits.
#
# If the function is passed a valid PIN string, return true, else return false.
#
# Examples (Input --> Output)
# "1234"   -->  true
# "12345"  -->  false
# "a234"   -->  false


# MY SOLUTION

def validate_pin(pin):
    final_test = ''
    for i in pin:
        if i.isdigit():
            final_test += i
        else:
            return False
    if (len(final_test) == 4) or (len(final_test) == 6):
        return True
    else:
        return False


# DEMONSTRATION

print(validate_pin("123 "))
print(validate_pin("0000"))
print(validate_pin("+2384"))
print(validate_pin("1234"))
print(validate_pin('-44444'))
