import sys


def printField(f, rows):
	for c in range(rows):
		print(''.join(f[c]))

def main():
	lines = sys.stdin

	if len(sys.argv) > 1:
		f = open(sys.argv[1], "r")
		lines = f.readlines()


	imgdata = lines[0]
	layers = []
	bestlayer = None
	i = 0
	minz = 99999
	while i < len(imgdata)-1:	
		z = 0
		o = 0
		t = 0
		for j in range(25*6):
			if (imgdata[i+j] == '1'):
				o += 1
			if (imgdata[i+j] == '2'):
				t += 1
			if (imgdata[i+j] == '0'):
				z += 1
		if minz > z:
			minz = z
			bestlayer = t * o
		
		layers.append(imgdata[i:i+25*6-1])
				
		i += 25*6

	print(bestlayer)

	field = [['?'] *24 for x in range(6)]

	for y in range(6):
		for x in range(24):
			for l in layers:
				if l[y*25+x] != "2":
					field[y][x] = " " if l[y*25+x] == "0" else "X"
					break
		


	printField(field, 6)

if __name__== "__main__":
	main()
