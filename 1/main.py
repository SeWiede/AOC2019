import sys

def main():
	lines = sys.stdin

	if len(sys.argv) > 1:
		f = open(sys.argv[1], "r")
		lines = f.readlines()
	
	x = 0
	for line in lines:
		if len(line) > 0:
			try:
				y = int(line)
			except Exception as ex:
				pass
			
			while y/3-2 > 0:
				y = y/3-2
				x+=y
				
	print x



if __name__== "__main__":
	main()
