import sys
import itertools
import subprocess
import math

from vm import vm

import time

black = 0#"."
white = 1#"#"
UP="^"
DOWN="v"
LEFT="<"
RIGHT=">"

def getDir(s, l):
	if s == UP:
		return LEFT if l == 0 else RIGHT
	if s == DOWN:
		return RIGHT if l==0 else LEFT
	if s == RIGHT:
		return UP if l == 0 else DOWN
	if s == LEFT:
		return DOWN if l==0 else UP

def getNewPos(pos, s):
	if s == UP:
		return (pos[0], pos[1]-1)
	if s == DOWN:
		return (pos[0], pos[1]+1)
	if s == RIGHT:
		return (pos[0]+1, pos[1])
	if s == LEFT:
		return (pos[0]-1, pos[1])

def printField(f):
	for row in f:
		print(''.join(map(lambda x: '#' if x == 1 else ' ' if x == 0 else x, row)))

def main():
	lines = sys.stdin

	if len(sys.argv) > 1:
		f = open(sys.argv[1], "r")
		lines = f.readlines()

	size= 99
	field = [[black] * size for x in range(size)]
	drawnL = []
	pos = (math.floor(size/2), math.floor(size/2))
	d = UP

	p = vm(lines)
	p.send(None)
	ns = 0	
	while True:
		y = pos[1]
		x = pos[0]
		
		#p.stdin.write((str(field[y][x])+"\n").encode())
		try:
			color = p.send(field[y][x])
			direction = next(p)
			TEST= next(p)
		except:
			break

		#out = readProg(p)
		if pos not in drawnL:
			drawnL.append(pos)	
		field[y][x] = color
		d = getDir(d, direction)
		pos = getNewPos(pos, d)
		
	print(len(drawnL))

if __name__== "__main__":
	main()
