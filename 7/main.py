import sys
import itertools
import subprocess


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

	maxthrust = 0
	maxperm= []
	for cl in perms2:
		A = startAmp(cl[0])
		B = startAmp(cl[1])
		C = startAmp(cl[2])
		D = startAmp(cl[3])
		E = startAmp(cl[4])
		print("test write")
		A.stdin.write((str(0)+"\n").encode())
		B.stdin.write("0\n".encode())
		D.stdin.write("0\n".encode())
		print("test write done")
		print(A)
		AAmp = getAMPProg(A, 0)
		BAmp = getAMPProg(B, AAmp)
		CAmp = getAMPProg(C, BAmp)
		DAmp = getAMPProg(D, CAmp)
		EAmp = getAMPProg(E, DAmp)
		print("init done")
		while True:
			AAmp = getAMPProg(A, EAmp)
			BAmp = getAMPProg(B, AAmp)
			CAmp = getAMPProg(C, BAmp)
			DAmp = getAMPProg(D, CAmp)
			EAmp = getAMPProg(E, DAmp)
			if E.poll() != None:
				break	
		if EAmp > maxthrust:
			maxthrust = EAmp
			maxperm = cl
		

	print(maxthrust)
	print(cl)

if __name__== "__main__":
	main()
