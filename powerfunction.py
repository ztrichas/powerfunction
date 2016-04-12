def int_input(prompt):
	answer = raw_input(prompt)
	
	try:
		return int(answer)
	except ValueError:
		return int_input("That wasn't a number. Try again.")
		
def float_input(prompt):
	answer = raw_input(prompt)
	
	try:
		return float(answer)
	except ValueError:
		return int_input("That wasn't a number. Try again.")

def recursivePowerFunction(base, exponent):

	if exponent == 0:
		return 1 
		
	return base * recursivePowerFunction(base, exponent - 1)
	

