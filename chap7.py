# Enter your answrs for chapter 7 here
# Name: Patrick Kennedy


# Ex. 7.5

import math

#thank god for discrete math
def combinatoric(x):
	if x == 0:
		return 1
	else:
		holder = combinatoric(x-1)
		passback = x + holder
		return passback

def closeTopie():
	#grabbed this from wikipedia.org/wiki/Pi
	total = 0
	k = 0
	counter = 0
	factor = 2*math.sqrt(2)/9801
	while True:
		num = combinatoric(4*k)*(1103+26390*k)
		den = combinatoric(k)**4 * 396**(4*k)
		term = factor * num/den
		total += term
		counter = counter +1
		if abs(term) < 1e-15: break
		k += 1
	print counter	#prints the number of loops
	return 1/total

#this prints the calc and gets us close to Pi
print closeTopie()




# How many iterations does it take to converge?
# I think it takes 4 passes