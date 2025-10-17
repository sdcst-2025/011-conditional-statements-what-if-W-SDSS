#! python3

"""
Have the user enter in a sentence. 
Check to see if the word "password" is located in the sentence

Inputs:
a sentence

Outputs:
"the sentence contains password"
"the sentence does not contain password"

Examples:
Enter a sentence: I will not buy this record, it is scratched.
the sentence does not contain password

Enter a sentence: The best password is no password.
the sentence contains password
"""

sentense = input("Enter a sentense: ")

if "password" in sentense:
    print("the sentense contains password")
else:
    print("the sentense does not contain password")