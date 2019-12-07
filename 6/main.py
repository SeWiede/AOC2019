import sys

class Planet:
	o = []
	name = None
	depth = 0
	parent = None
	def __init__(self, name = "invalid", parent = None, oe = None):
		self.name = name
		self.o = []
		self.parent= parent
		if oe != None:
			self.o.append(oe)
		self.depth = 0

	def incDepth(self, x):
		self.depth += x
		for p in self.o:
			p.incDepth(x)

	def __str__(self):
		return self.name + "(" + str(self.depth) + "):["+ str(self.parent) +"]"

def main():
	lines = sys.stdin

	if len(sys.argv) > 1:
		f = open(sys.argv[1], "r")
		lines = f.readlines()


	#build planets and direct orbits constilation	
	planets=[]
	for line in lines:
		line = line[0:len(line)-1]
		pls = line.split(")", -1)
		if len(pls) < 2:
			break
		p = pls[0]
		o = pls[1]
		pl = []
		ol = []
		
		#see if mentioned planets are alrdy registered	
		curP = next((x for x in planets if x.name == p), None)
		op = next((x for x in planets if x.name == o), None)		

		#if orbiting one isnt seen yet create it and add it to list
		if op == None:
			op = Planet(o, p)
			planets.append(op)
			op.depth += 1

		#if the parent planet already exist in planet list 
		#just add the orbiting one to its orbit list
		if curP != None:
			curP.o.append(op)
		#otherwise create it and add afterwards
		if curP == None:
			curP = Planet(p, None, op)
			planets.append(curP)		

		#add indirect orbit depth and if the orbiting one does not
		#have a parent yet recursively add depth to its orbit ones 
		op.depth += curP.depth
		if op.parent == None:
			op.parent = curP.name
			op.depth += 1
			for tempp in op.o:
				tempp.incDepth(op.depth)
	

	orbits = 0
	for p in planets:
		#print(p)
		orbits += p.depth
	print(str(orbits))

if __name__== "__main__":
	main()