

import random

def getGCF(number1, number2):
	GCF = 0 
	if number1 > number2:
		GCF = number2
	else:
		GCF = number1
	
	while (number1 % GCF != 0) or (number2 % GCF != 0):
		GCF = GCF - 1 
		
	return GCF		


def largest(number1, number2, number3, number4):
	largestNum = 0
	
	if (number1 > number2) and (number1 > number3) and (number1 > number4):
		largestNum = number1
	elif (number2 > number1) and (number2 > number3) and (number2 > number4):
		largestNum = number2
	elif (number3 > number1) and (number3 > number2) and (number3 > number4):
		largestNum = number3
	else:
		largestNum = number4
	return largestNum


def magic8ball():
	a = (random.random())
	if a >= .0 and a < 1.0 / 9: 
		return "It is certain"
	elif a >= .1 and a < 2.0 / 9:
		return "Yes, definitely"
	elif a >= .2 and a < 3.0 / 9:
		return "Yes"
	elif a >= .3 and a < 4.0 / 9:
		return "Not sure. Ask again later"
	elif a >= .4 and a < 5.0 / 9:
		return "Concentrate and ask again"
	elif a >= .5 and a < 6.0 / 9:
		return "Reply hazy try again"
	elif a >= .6 and a < 7.0 / 9:
		return "No"
	elif a >= .7 and a < 8.0 / 9:
		return "Certainly not"
	elif a >= .8 and a < 9.0 / 9: # This value needs to be equal with everything else 
		return "Doubtful"
	
def myName():
	return ("__________             .__  \n\____    /____    ____ |  |__ \n  /     /\__  \ _/ ___\|  |  \  \n /     /_ / __ \\  \____|   Y  \  \n/_______ (____  /\___  >___|  /  \n        \/    \/     \/     \/  ")



def alphaOrder(string1, string2):
	for i in range(0, len(string1)):
		if ord(string1[i].lower()) < ord(string2[i].lower()):
			return string1 + " " + string2
		elif ord(string2[i].lower()) < ord(string1[i].lower()):
			return string2 + " " + string1
		if i == len(string2):
			return string2 + " " + string1
	
	
def zipStrings(string1, string2):
	zippedString = ""
	index = 0 
	maxlength = 0
	
	if len(string1) > len(string2):
		maxlength = len(string1)
	else:
		maxlength = len(string2)
		
	while index < maxlength:
	
		if index < len(string1):
			zippedString = zippedString + string1[index]
		
		if index < len(string2):
			zippedString = zippedString + string2[index]
		
		index = index + 1	
	
	return zippedString

def everyOther(string):
	newString = ""
	index = 0 
	
	while (index < len(string)):
		
		if index % 2 == 0:
			newString = newString + string[index] 
			
		index += 1
	
	return newString
		
		
def countLower(string):
	counter = 0
	for i in string:
		if i.isalpha() == True:
			if i.islower() == True:
				counter += 1
	return counter
			


def xEncrypt(string):
	decryptedWord = ""
	index = 0
	while index < len(string):	
		if string[index] == "x" and (index + 1) != len(string):
			decryptedWord = decryptedWord + string[index + 1]
		index = index + 1
	
	return decryptedWord

	
	
			
			








