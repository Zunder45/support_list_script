import argparse

str = ""
space = False

def scan_chars(list):
	global str
	list_char = ["\'", "\""]

	for i in list_char:
		for num, j in enumerate(list):
			str += i + j + i 
			if num != len(list)-1:
				str += ","
		str += "\n"
	print(str.lower())
	print(str.upper())

def pars(): 
	parser = argparse.ArgumentParser()
	parser.add_argument("-s","--nospace",help="length", action="store_const", const="True")
	arg = parser.parse_args()
	print(arg.nospace)
	if arg.nospace:
		global space
		space = arg.nospace


def main():
	pars()
	list = input("input text: ") 
	global space
	if space:
		list = list.replace(" ","")
	scan_chars(list)

main()