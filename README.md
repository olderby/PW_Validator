# Password Validator
a small script to validate a password for characters

## Project Description
This projects applys theory learned to validate password using RegEx module. This project is for learning purposes
make this adaptable in the future to optionally validate things

## Usage
To clone this repository

navigate to your project folder

From the command line:
    'git clone https://github.com/olderby/PW_Validator.git'

testing:
run tests from root using unittest
    `pythonX -m unittest discover -s tests`

[I know these tests aren't fully working will fix shortly.]: #

## Examples

#### Accepted passowrd
<code>
    Enter your Password: passworddogName23&&
    Passowrd Accepted
</code>

#### Failure to validate
<code>
    Enter your Password: passwor
    Passowrd must contain a numeric digit
</code

## Change Log
    v0.0.1 Added rules.json file to configure validation rules. Adjusted validation rules for more validation criteria
    * pending adding disallowed patterns list and dictionary words via rules.json
    * writing tests for validation rules, rules.json configuration edge cases
        - started writing tests todo items for tests:
            breakdown tests into smaller granularity
            more tests for missing attributes, missing keys, malformed attributes
            put file clean up in dedicated tearDown() method and use error handling
    * Create pull request on my own self for self review (because I can)

## TODO:
1. Implement Graceful handling of malformed json files, even for test cases
2. Implement password and salt storage in secure (encrypted) file