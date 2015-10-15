pal_dict = {}
keep_going = True
escape = "!q"

#Asks the user for a string, if it matches the escape string, the program ends.
def query():
    print "\nPlease enter your string:"
    input_string = str(raw_input())
    if input_string == escape:
        keep_going = False
    else:
        return input_string


#Check to see if the string is a palindrome, omitting case, punctuation and spaces.
def is_palindrome(x):
    punc = '''
           !@#$%^&*()_+|~`\=-{}"<>?[]',./ "
           '''
    check_string  = x.lower()
    check_string = check_string.translate(None, punc)
    reversed_string = check_string[::-1]
    if check_string == reversed_string:
        return True
    else:
        return False


#Take the string, check if it's in the dictionary and add it and it's palindrome state if not.
def check_dict(x):
    if x not in pal_dict.keys():
        pal_dict[x] = is_palindrome(x)
        print "New entry added"
    else:
       print "Entry found in dictionary."


    if pal_dict[x]:
        print "It's a palindrome!"
    else:
        print "Not a palindrome!"

print "Welcome to the palindrome detector! Type !q to quit."
while keep_going == True:
    check_dict(query())
