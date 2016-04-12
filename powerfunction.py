#Call on the fucntion to keep doing it 

#Write tests and make sure function is recursive
#Write a main program that uses a recursive int_input and float input

def recursivePowerFunction(base, exponent):
	#if base == 0:
	#	return 0
	if exponent == 0:
		return 1 
		
	#if exponent == 1: #Terminating case
	#	return base
	return base * recursivePowerFunction(base, exponent - 1)

#Create a main program with the float input and int input 
#Ask tom about the int input function

base = float_input("Input a base.")
exponent = int_input("Input an exponent.")

print( recursivePowerFunction(base, exponent))