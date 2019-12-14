import sys
import itertools
import subprocess

sys.path.insert(1, '../11/')
from vm import vm

def getAMP(setting, AMP):
	prog = subprocess.Popen(["python", "../5/main.py", sys.argv[1]],
							stdin=subprocess.PIPE,
							stdout=subprocess.PIPE)
	prog.stdin.write(str(setting)+"\n")
	prog.stdin.write(str(AMP) + "\n")

	
	ret = -1
	x = ""
	try:
		x = prog.stdout.readline()
		ret = int(x)
	except:
		print(x)

	return ret

def startAmp(setting):
	prog = subprocess.Popen(["python3", "../5/main.py", sys.argv[1]],
							stdin=subprocess.PIPE,
							stdout=subprocess.PIPE)
	prog.stdin.write((str(setting)+"\n").encode())
	return prog

def getAMPProg(p, AMP):
	print(p)
	p.stdin.write((str(AMP) + "\n").encode())
	ret = 0
	x = ""
	try:
		x = p.stdout.readline()
		ret = int(x)
	except:
		print("Error while reading programs stdout")

	return ret

def main():
	
	perms = list(itertools.permutations([0,1,2,3,4]))
	perms2 = list(itertools.permutations([5,6,7,8,9]))
	test = [0,1,2,3,4]	

	lines = sys.stdin

	if len(sys.argv) > 1:
		f = open(sys.argv[1], "r")
		lines = f.readlines()


	maxthrust = 0
	maxperm= []
	for cl in perms2:
		A = vm(lines)
		next(A)
		B = vm(lines)
		next(B)
		C = vm(lines)
		next(C)
		D = vm(lines)
		next(D)
		E = vm(lines)
		next(E)
		A.send(cl[0])
		B.send(cl[1])
		C.send(cl[2])
		D.send(cl[3])
		E.send(cl[4])
		AAmp = A.send(0)
		BAmp = B.send(AAmp)
		CAmp = C.send(BAmp)
		DAmp = D.send(CAmp)
		EAmp = E.send(DAmp)
		while True:
			try:
				next(A)
				next(B)
				next(C)
				next(D)
				next(E)
				AAmp = A.send(EAmp)
				BAmp = B.send(AAmp)
				CAmp = C.send(BAmp)
				DAmp = D.send(CAmp)
				EAmp = E.send(DAmp)
			except:
				break
		if EAmp > maxthrust:
			maxthrust = EAmp
			maxperm = cl
		

	print(maxthrust)
	print(cl)

if __name__== "__main__":
	main()
