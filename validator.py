# using regex for the win it's easier
import re
import json


# validate password has at least length or 8 by default characters
def validate_length(password, max, min=8):
    if len(password) < min:
        print("Password is too short!")
        if len(password) > max:
            print("Password is too long!")
            return False
        return False
    else:
        return True
    
# validate password contains lower case letters
def validate_lower(password):
    test1 = re.findall("[a-z]", password)
    if test1:
        return True
    else:
        return False
    
# validate password contains uppercase and lower case letters
def validate_upper(password):
    test1 = re.findall("[A-Z]", password)
    if test1:
        return True
    else:
        return False

# validate password has at least 1 numeric digit
def validate_numeric(password):
    test = re.findall("[0-9]", password)
    if test:
        return True
    else:
        return False

# validate at least one special character
def validate_special(password):
    test1 = re.findall("[^A-Za-z0-9]", password)
    if test1:
        return True
    else:
        return False

# read rules from JSON config file
def read_config():
    config_file = open("rules.json", "rt")
    config = json.loads(config_file.read())
    return config



# run all validation tests
def full_test(password, config_rules):
    # track the validation of the passowrd
    valid = True
    if validate_length(password, config_rules["maximum_length"], config_rules["minimum_length"]) == False:
        valid = False
    if validate_lower(password) == False and config_rules["lower_case"]:
        print("\nPassword must contain lower case")
        valid = False
    if validate_upper(password) == False and config_rules["upper_case"]:
        print("\nPassword must contain upper case")
        valid = False
    if validate_numeric(password) == False and config_rules["numbers"]:
        print("\nPassword must contain a numeric digit")
        valid = False
    if validate_special(password) == False and config_rules["special_char"]:
        print("Password must contain a special character")
        valid = False
    #If the password is still valid show that it was accepted
    if valid:
        print("\nPassowrd Accepted")

config_rules = read_config()

full_test(input("Enter your Password: "), config_rules)

