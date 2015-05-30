def isPalindrome(string):
	if string == string[::-1]:
		return True
	else:
		return False

def stringRotations(string):
	rotationsList = list()

	for iterator in range(len(string)):
		part1 = string[0:iterator]		
		part2 = string[iterator:len(string)]
		
		rotationsList.append(part2 + part1)
	
	return rotationsList

def parseInput(string):
	rotationsList = stringRotations(string)

	hasPalindrome = False

	for rotationString in rotationsList:
		if isPalindrome(rotationString):
			hasPalindrome = True
			print rotationString
		
	if hasPalindrome == False:
		print 'NONE'

parseInput(raw_input())
