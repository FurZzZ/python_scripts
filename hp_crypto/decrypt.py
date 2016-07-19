__author__ = "FurZzZ"

'''
crypto from rozwal.to
http://212.71.244.194/hp31337/crypto/crypto.html
All of base64 sentences are: plain_text ^ key where key is always the same, so lets brute force it!
'''

import base64, sys

def validateResult(bruteForcedResult):
	return False


def getPlainFromBase64(b64string):
	return base64.b64decode(b64string)


def checkIfContainsCharsAndNumbers(string):
	pass

def tryToGetPlain(string):
	pass

def checkInput():
	if len(sys.argv) > 1:
		if sys.argv[1].isdigit():
			print sys.argv[1]
			return sys.argv[1]
		else:
			print "Only numbers allowed! \r\nUsage: python decrypt.py key_length\r\nExample: python decrypt.py 22"	
			return False

def bruteForceThis(stringInHex, max_chars):
	#prepare list of lists with all Ascii chars
	tmpArray = [None] * int(max_chars)
	tmpArray = [z for z in range(0, int(max_chars))]
	for i in range(0,int(max_chars)):
		tmp = [chr(x) for x in range(32, 127)]
		tmpArray[int(i)] = tmp

	print len(tmpArray),


def main():
	tab_b64 = ['Zv0LKbgwQ+xwVPxHJLgdDO55UOpHIfcVD+NnHbgGZfwWD+50Q7gONrgOC+NhEdFHK/0cBw==', 'cPYDZe8RBvBwEeEIMLgOAux7ULgAKrgNC+tmEewOKP0=',
	 'ZfAVIP1ZBet7Vv0VNrgQDaJhWf1HLfcXBvt2XvUF', 'cPEJYuxZAqJiUOFHMfdZEOp0Wv1HMfAcQ+VnXu0JIbgwQ+BgWPQTZfocBe1nVLgeKu1ZAON4VLgTKrgbBg==',
	 'c+0TZewRBqJhQ+0TLbgQEKJsXu1HIfcXRPY1WfkRILgNC+c1QuwIKPkaC6JhXrgAIOxZBu8=', 'cPYDZeEWFqJlXfkeIPxZCvY1RfdHMfAcQ+BwUOw=', 
	 'Y/0KKu4cQ+5wRewCN+tZO6JzQ/cKZewRBqJmReoOK/9ZAuxxEfUCJPoAQ/t6RLgQLPQVQ/V8X7g1HdchOdpCadkrHcchGNpaafY/IMAtO+tNXMACHcghV9pxae8/dcBJO/ZoabgoLqc=',
	'cvcXPOoQBOphVPxHJ+FZF+pwWOpHN/0KE+d2RfERILgYFvZ9XuoU', 'aPcSZfYcBuY1RfdHJO0NC+d7RfEEJOwc', 'aPcSZfcXD/s1WfkRILgYQ+RwRrgUIPsWDeZmEewIZesWD/RwEf0GJvBZEvdwQuwOKvY=', 'cOoTZfcfQ+dtQfQILOwYF+t6Xw==']

	maximumKeySize = checkInput()
	if maximumKeySize == False:
		sys.exit()
	else:
		print "max key size = " + str(maximumKeySize)
		for currentTabElement in tab_b64:
			for currMaxKeySize in range(0,int(maximumKeySize)):
				#temporaryResult = validateResult(bruteForceThis(getPlainFromBase64(currentTabElement), currMaxKeySize))
				test = bruteForceThis(getPlainFromBase64(currentTabElement), currMaxKeySize)
				#print test
				# if temporaryResult != False:
				# 	print temporaryResult
					#from 32 to 126
			# temporary_result = ""
			# x = getPlainFromBase64(i)
			# for z in x:
			# 	print str(ord(z)) + " " + str(z)	
			print ""
			

if __name__ == "__main__":
	main()
	# for i in range(32,127):
	# 	print chr(i)