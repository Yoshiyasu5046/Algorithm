# Define a procedure is_palindrome, that takes as input a string, and returns a
# Boolean indicating if the input string is a palindrome.

# Base Case: '' => True
# Recursive Case: if first and last characters don't match => False
# if they do match, is the middle a palindrome?

# Recursive solution

def palindrome_recursive(s):
    if s == '' or s == "":
        return True
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False
 
 
print palindrome_recursive('')
#>>> True
print palindrome_recursive('abab')
#>>> False
print palindrome_recursive('abba')
#>>> True


# Loop solution

def palindrome_loop(s):
	for i in range(0, len(s)/2):
		if s[i] != s[-(i + 1)]:
			return False
		return True

 
print palindrome_loop('')
#>>> True
print palindrome_loop('abab')
#>>> False
print palindrome_loop('abba')
#>>> True