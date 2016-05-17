__author__ = "FurZzZ"

'''
The link that help me to find the right solution:
http://www.darkside.com.au/snow/

Whitespace Steganography
'''

def getCodesFromLines(file):
	# Our return code
	code_from_snow = []

	# As snow documentation state let's extract data from text:
	for line in file:
		if line.find(' \n') != -1:
			code_from_snow.append('1')
		else:
			code_from_snow.append('0')
	# It will return something like 101010101010101011011100
	str = ''.join(code_from_snow)
	return str

# Decode the string
def getTheFlag(str):
	flag = []
    
	for i in range(len(str)/8):
		temporary = []

		for j in range(8):
			temporary.append(str[i * 8 + j])

		num = ''.join(temporary)
		# We get bin values of the letters (in ASCII table) so we have to convert them to text
		binToDec = int(num, 2)

		# Now we can change it to text by using a ASCII codes
		decToText = chr(binToDec)
		
		flag.append(decToText)

	return ''.join(flag)


file = open('snow.txt', 'r')
print getTheFlag(getCodesFromLines(file))