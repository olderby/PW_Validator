# using regex for the win it's easier
import re


#write validation rules
    #validate password has at least 8 characters
def validate_length(password, length=8):
    if len(password) > length:
        return True
    else:
        return False
    #validate password containes both uppercase and lower case letters
def validate_case(password):
    test1 = re.findall("[A-Z]", password)
    test2 = re.findall("[a-z]", password)
    if test1 and test2:
        return True
    else:
        return False
    #validate password has at least 1 numeric digit
def validate_numeric(password):
    test = re.findall("[0-9]", password)
    if test:
        return True
    else:
        return False
    #validate at least one special character
def validate_special(password):
    test1 = re.findall("[^A-Za-z0-9]", password)
    if test1:
        return True
    else:
        return False


def full_test(password):
    #track the validation of the passowrd
    valid = True
    if validate_length(password,  8) == False:
        print("\nPassword too short")
        valid = False
    if validate_case(password) == False:
        print("\nPassword must contain upper and lower case")
        valid = False
    if validate_numeric(password) == False:
        print("\nPassword must contain a numeric digit")
        valid = False
    if validate_special(password) == False:
        print("Password must contain a special character")
        valid = False
    #If the password is still valid show that it was accepted
    if valid:
        print("\nPassowrd Accepted")

full_test(input("Enter your Password: "))