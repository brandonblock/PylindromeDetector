pal_dict = {}
keep_going = True
escape = "!q"
punc = '''
       !@#$%^&*()_+-={}|"<>?[]\;:',./
       '''
#Asks the user for a string and formats it for checking, the program ends if it matches the escape string.
def query():
    print("\nPlease enter your string:")
    input_string = str(input())
    if input_string == escape:
        keep_going = False
    else:
        input_string = input_string.translate(punc)
        return input_string.lower()

#Check to see if the string is a palindrome, omitting case, punctuation and spaces.
def is_palindrome(x):
    check_string  = x
    reversed_string = check_string[::-1]
    if check_string == reversed_string:
        return True
    else:
        return False


#Take the string, check if it's in the dictionary and add it and its palindrome state if not.
def check_dict(x):
    if x not in list(pal_dict.keys()):
        pal_dict[x] = is_palindrome(x)
        print("New entry added")
    else:
       print("Entry found in dictionary.")


    if pal_dict[x]:
        print("It's a palindrome!")
    else:
        print("Not a palindrome!")

print("Welcome to the palindrome detector! Type !q to quit.")
while keep_going:
    check_dict(query())
