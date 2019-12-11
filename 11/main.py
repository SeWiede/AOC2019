import sys
import itertools
import subprocess
import math

black = 1#"."
white = 0#"#"
UP="^"
DOWN="v"
LEFT="<"
RIGHT=">"

def startProg():
	prog = subprocess.Popen(["python3", "../9/main.py", sys.argv[1]],
							stdin=subprocess.PIPE,
							stdout=subprocess.PIPE)
	return prog

def writeProg(p, s):
	print("writing...")

def readProg(p):
	color = p.stdout.readline()
	direction = p.stdout.readline()
	try:
		return (int(color), int(direction))
	except:
		print(color, direction)
		print("error while reading from prog", file=sys.stderr)

def getDir(s, l):
	if s == UP:
		return LEFT if l == 0 else RIGHT
	if s == DOWN:
		return RIGHT if l==0 else LEFT
	if s == RIGHT:
		return UP if l == 0 else DOWN
	if s == LEFT:
		return DOWN if l==0 else UP

def getNeswPos(pos, d):
	if s == UP:
		return (pos[0], pos[1]-1)
	if s == DOWN:
		return (pos[0], pos[1]+1)
	if s == RIGHT:
		return (pos[0]+1, pos[1])
	if s == LEFT:
		return (pos[0]-1, pos[1])

def main():
	size= 999
	field = [[black] * size for x in range(size)]
	drawnL = []
	pos = (math.floor(size/2), math.floor(size/2))
	d = UP
	#p = startProg()
	p = subprocess.Popen(["python3", "../9/main.py", sys.argv[1]],
							stdin=subprocess.PIPE,
							stdout=subprocess.PIPE, bufsize=100)
	
	while p.poll() == None:
		y = pos[1]
		x = pos[1]
		#writeProg(p, field[y][x])
		print("writing...")
		p.stdin.write((str(field[y][x])+"\n").encode())
		print("reading...")
		
		color = p.stdout.readline(1)
		print("reading...")
		direction = p.stdout.readline(1)
		print("done")
		try:
			out = (int(color), int(direction))
		except:
			print(color, direction)
			print("error while reading from prog", file=sys.stderr)
		
		#out = readProg(p)
		if pos not in drawnL:
			drawnL.append(pos)
		field[y][x] = out[0]
		newd = getDir(d, out[1])
		getNeswPos(pos, newd)

	print(len(drawnL))

if __name__== "__main__":
	main()
