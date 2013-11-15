# Enter your answrs for chapter 6 here
# Name: Patrick Kennedy


# Ex. 6.6
#returns the first letter
def first(word):
	return word[0]
#returns the last letter
def last(word):
	return word[-1]
#returns everything in between first and last
def middle(word):
	return word[1:-1]


#function to determine if a palendrome is present
def is_palindrome(word):
	length = len(word)
	
	if (first(word) == last(word)):
		#print 'we have a palindrome!'
		return True
	else:			
		#print 'Its not a palindrome!'
		return False
	return is_palindrome(middle(word))
	
def Test_Run(word): #this was to test the below items individually through the functions
	print first(word)
	print last(word)
	print middle(word)

passIn = 'Baboon'
passIn2 = 'redivider'
test1 = '' #results in an error
test2 = 'B' #no issues, but the last and first only print out and middle does not generate
test3 = 'CC' #no issues, middle does not print

#Test_Run(test2)
#length = len(passIn2)
#print length
#print passIn2[1:-1]

print is_palindrome(passIn)
print is_palindrome(passIn2)
print is_palindrome(test2)
print is_palindrome(test3)



# Ex 6.8

#greatest common denominator/divisor/whatever

#courtesy of Wikipedia:
def gcd(a, b):
	if (b == 0):
		return a
	else:
		return gcd (b, (a%b))
	




print "Now for the Greatest Common Divisor"
print gcd(100, 101)













