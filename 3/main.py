import sys


def crossed(pT1, t1, pT2, t2):
	if (t1[2] == "R" or t1[2] == "L") and (t2[2] == "R" or t2[2] == "L") or (t1[2] == "U" or t1[2] == "D") and (t2[2] == "U" or t2[2] == "D"):
		return False 

	if pT1[0] == t1[0]: #x is equal
		if ((pT2[0] >= t1[0] and t2[0] <= t1[0]) or (pT2[0] <= t1[0] and t2[0] >= t1[0])) and ((t2[1] <= pT1[1] and t2[1] >= t1[1]) or (t2[1] >= pT1[1] and t2[1] <= t1[1])):
			return True	
	else: #y is equal
		 if ((pT2[1] >= t1[1] and t2[1] <= t1[1]) or (pT2[1] <= t1[1] and t2[1] >= t1[1])) and ((t2[0] <= pT1[0] and t2[0] >= t1[0]) or (t2[0] >= pT1[0] and t2[0] <= t1[0])):
			return True	
	return False

def getCross(pT1, t1, pT2, t2):
	if pT1[0] == t1[0]: #x is equal
		return (t1[0], t2[1])
	else: #y is equal 
		return (t2[0], t1[1])

def getStepsToCross(pT1, t1, pT2, t2):
	if pT1[0] == t1[0]: #x is equal
		return abs(pT1[1] - t2[1]) + abs(pT2[0] - t1[0])
	else: #y is equal 
		return abs(pT1[0] - t2[0]) + abs(pT2[1] -t1[1])

def getTurns(turns, wire):
	posX = 0
	posY = 0
	idx = 0
	for p in wire:
		d = p[0]
		l = int(p[1:])
		xDir = 0
		yDir = 0
		if d == "R":
			xDir = 1
		if d == "L":
			xDir = -1
		if d == "D":
			yDir = -1
		if d == "U":
			yDir = 1
		posX = posX + xDir*l
		posY = posY + yDir*l
		steps = abs(xDir*l + yDir*l)
		turns.append((posX,posY, d, steps))
		idx += 1

def main():
	lines = sys.stdin

	if len(sys.argv) > 1:
		f = open(sys.argv[1], "r")
		lines = f.readlines()

	
	wire1 = lines[0].split(",", -1)
	wire2 = lines[1].split(",", -1)

	turns1 = []
	turns2 = []
	
	getTurns(turns1, wire1)		
	getTurns(turns2, wire2)		

	minDist = 99999
	minDistSteps = 99999
	x = None
	minSteps = 99999
	pT1 = (0,0,turns1[0][2], 0)
	pT2 = (0,0,turns2[0][2], 0)
	stepsT1 = 0
	idx1 =-1
	idx2 =-1
	for t1 in turns1:
		idx2=-1
		idx1+=1
		stepsT1 += t1[3]
		steps = stepsT1
		for t2 in turns2:
			idx2+=1
			steps += t2[3]			
			if crossed(pT1, t1, pT2, t2):
				xtemp = getCross(pT1, t1, pT2, t2)
				if not (xtemp[0] == 0 and xtemp[1] == 0):
					stc = getStepsToCross(pT1, t1, pT2, t2)
					tempsteps = steps - t1[3] - t2[3] + stc
					dtemp = abs(xtemp[0]) + abs(xtemp[1])
					if dtemp < minDist:
						x = xtemp
						minDist = dtemp
						minDistSteps = tempsteps
					if tempsteps < minSteps:
						minSteps = tempsteps
			pT2 = t2
		pT1 = t1 

	print(x, minDist,minDistSteps, minSteps)

if __name__== "__main__":
	main()











































