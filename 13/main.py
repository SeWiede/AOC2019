import sys
import itertools
import subprocess
import math

sys.path.insert(1, '../11/')
from vm import vm

import time


E=0
W=1
BL=2
H=3
B=4

def printField(f):
	for row in f:
		print(''.join(map(lambda x: "E" if x ==E else "W" if x == W else "B" if x==BL else "H" if x == H else "O" if x == B else "?", row)))

def main():
	lines = sys.stdin

	if len(sys.argv) > 1:
		f = open(sys.argv[1], "r")
		lines = f.readlines()


	field = [[-1]*44 for x in range(20)]	
	p = vm(lines)
	i = 0
	blocks=0
	ballpos = ()
	paddlepos = ()
	for i in range(44*20):
		try:
			x = next(p)
			y = next(p)
			id = next(p)
			field[y][x] = id
			if(id ==3):
				paddlepos=(x,y)
			if(id ==4):
				ballpos=(x,y)
			blocks += 0 if id != 2 else 1
		except:
			break
		i+=1
	print(i, blocks, ballpos)

	points = 0
	px = 0
	py = 0
	up = False
	while True:
		movr = False
		movl = False
		dx = ballpos[0]-paddlepos[0]		
		dy = ballpos[1]-paddlepos[1]
		px=0	
		try:
			if up:
				if dx > 0 and paddlepos[0] < 43:
					movr = True
					x=p.send(1)
				if dx < 0 and paddlepos[0] > 1:
					movl = True
					x=p.send(-1) 
			if not up and dx < 0:
				if abs(dy) > 0 and paddlepos[0] > 1:
					movl = True
					x=p.send(-1)
			if not up and dx >0:
				#ball is right of paddle
				if abs(dy) > 0 and paddlepos[0] < 43:
					movr = True
					x=p.send(1)
			if not movr and not movl:
				x=p.send(0)
			y=next(p)
			v=next(p)
		except:
			break
		
		if x == -1 and y == 0:
			points = v
		if x == -99 or y == -99 or v == -99 or v != 4:
			continue

		up = py > y
		px = x
		py = y		

		field[paddlepos[1]][paddlepos[0]] = 0
		if movr:
			paddlepos = (paddlepos[0] +1, paddlepos[1])
		if movl:
			paddlepos = (paddlepos[0] -1, paddlepos[1])	
		field[paddlepos[1]][paddlepos[0]] = 3


		field[ballpos[1]][ballpos[0]] = 0
		ballpos = (x,y)
		field[ballpos[1]][ballpos[0]] = 4
		
		#printField(field)
		#sys.stdin.readline()

	print(points)

if __name__== "__main__":
	main()
