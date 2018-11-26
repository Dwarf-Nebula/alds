'''
———————————————————————————————————————————————
GITHUB --> https://github.com/Dwarf-Nebula/alds
———————————————————————————————————————————————

1720840
TICT_V1C / TCTI-V2ALDS1
'''

#2.1
"""
Rekent macht uit

Parameters
----------
f : int
factor
e : int
exponent

Return
------
m: int
uitkomst van f^e
"""
def machtv3(f, e):
	assert e > 0
	m = 1
	while e > 0:
		if e%2 == 0:
			m *= f * f
			e -= 2
		else:
			m *= f
			e -= 1
	return m

print("\n\n 2.1 \n")
for i in range (2, 11):
	for j in range(1, 10):
		#print("{macht:>10}{macht:<10}".format(macht = machtv3(i, j))) #kerstboom formaat :)
		print(machtv3(i, j))

"""
Rekent macht uit (recursief)

Parameters
----------
f : int
factor
e : int
exponent

Return
------
m: int
uitkomst van f^e
"""
#Does the same thing but with recursion
def recursion_machtv3(a, n):
	assert n > 0
	if (n==1):
		return a
	if n%2 == 0: #even
		n/=2
		return recursion_machtv3(a, n) * recursion_machtv3(a, n)
	else: #odd
		n-=1
		return a * recursion_machtv3(a, n)

print("\n\n 2.1, maar dan recursief \n")
for i in range (2, 11):
	for j in range(1, 10):
		print(recursion_machtv3(i, j))

#2.2
"""
Een class om een stack te maken
"""
class myStack(list):
	"""
	Zet iets op de stack

	Parameters
	----------
	item : nvt
	Het object dat je op de stack wilt zetten
	"""
	def push(self, item):
		self.append(item)
		
	"""
	Wat staat er bovenaan de stack

	Return
	------
	Het bovenste object van de stack
	"""
	def peek(self):
		return self[len(self)-1]
	
	"""
	Kijkt of de stack leeg is

	Return
	------
	: bool
	Is het een lege stack ja/nee
	"""
	def isEmpty(self):
		return len(self) == 0

print("\n\n 2.2 \n")
stack = myStack()
print(stack.isEmpty())
for i in range(10):
	stack.push(i)
print(stack.isEmpty())
print(stack.peek())
print(stack.pop())
print(stack.pop())

#2.3
"""
Kijkt of de haakjes die gebruikt worden in de goede volgorde staan

Parameters
----------
bracketString : string
De string waar de haakjes in staan

Return
------
: bool
Kloppen de haakjes ja/nee
"""
def areTheBracketsCorrect(bracketString):
	assert(type(bracketString) == str)
	stack2 = myStack()
	for bracket in bracketString:
		if (bracket == "(" or bracket == "{" or bracket == "[" or bracket == "<"):
			stack2.push(bracket)
		elif (stack2.isEmpty()):
			return False
		elif (bracket == ")"):
			if (stack2.pop() != "("):
				return False
		elif (bracket == "}"):
			if (stack2.pop() != "{"):
				return False
		elif (bracket == "]"):
			if (stack2.pop() != "["):
				return false
		elif (bracket == ">"):
			if (stack2.pop() != "<"):
				return False
	return stack2.isEmpty()

print("\n\n 2.3 \n")
print(areTheBracketsCorrect("[(<>)](){<()><>}((<>)())")) #True
print(areTheBracketsCorrect("(>")) #False
print(areTheBracketsCorrect("((")) #False
print(areTheBracketsCorrect(">"))  #False

#2.4
"""
Berekend de binaire waarde

Parameters
----------
n : int
Int waarvan de binaire waarde moet worden berekend

Return
------
: string
n als binaire waarde
"""
def myBin(n):
	assert(n >= 0)
	if n == 0: return "0b0"
	if n == 1: return "0b1"
	if (n%2): return myBin((n-1)/2) + "1"
	else: return myBin(n/2) + "0"

print("\n\n 2.4 \n")
for i in range(128):
	print("Decimal: {:>3}, myBin: {:>9}, pythonBin: {:>9}, equal = {}".format(i, myBin(i), bin(i), myBin(i) == bin(i)))

#2.5
import random

def isSorted(gesorteerdeLijst):
	for i in range(1, len(gesorteerdeLijst)):
		if (gesorteerdeLijst[i-1] > gesorteerdeLijst[i]):
			return False
	return True

"""
Sorteert een lijst

Parameters
----------
ongesorteerdeLijst : list
De lijst die gesorteerd moet worden

Links : int
De linker pointer

Rechts: int
De rechter pointer

Return
------
ongesorteerdeLijst: list
De lijst maar dan gesorteerd
"""
def quickSort(ongesorteerdeLijst, Links = 0, Rechts = -1):
	global p
	if(len(ongesorteerdeLijst)==1): return ongesorteerdeLijst
	if(Rechts == -1): Rechts = len(ongesorteerdeLijst)-1
	L = Links
	R = Rechts
	inhoudMidden = ongesorteerdeLijst[(Links + Rechts) // 2]
	while(L < R):
		while(ongesorteerdeLijst[L] < inhoudMidden):
			L+=1
			p+=1
		while(inhoudMidden < ongesorteerdeLijst[R]):
			R-=1
			p+=1

		if(L <= R):
			ongesorteerdeLijst[L], ongesorteerdeLijst[R] = ongesorteerdeLijst[R], ongesorteerdeLijst[L]
			L+=1
			R-=1
	if(Links < R): quickSort(ongesorteerdeLijst, Links, R)
	if(L < Rechts): quickSort(ongesorteerdeLijst, L, Rechts);
	return(ongesorteerdeLijst)

"""
Sorteert een lijst, maar dan op de slechtst mogelijke manier

Parameters
----------
ongesorteerdeLijst : list
De lijst die gesorteerd moet worden

Links : int
De linker pointer

Rechts: int
De rechter pointer

Return
------
ongesorteerdeLijst: list
De lijst maar dan gesorteerd
"""
def worstQuickSort(ongesorteerdeLijst, Links = 0, Rechts = -1):
	global worstP
	if(len(ongesorteerdeLijst)==1): return ongesorteerdeLijst
	if(Rechts == -1): Rechts = len(ongesorteerdeLijst)-1
	L = Links
	R = Rechts
	inhoudMidden = min(ongesorteerdeLijst[Links:Rechts])
	#inhoudMidden = ongesorteerdeLijst[Links]
	while(L < R):
		while(ongesorteerdeLijst[L] < inhoudMidden):
			L+=1
			worstP+=1
		while(inhoudMidden < ongesorteerdeLijst[R]):
			R-=1
			worstP+=1

		if(L <= R):
			ongesorteerdeLijst[L], ongesorteerdeLijst[R] = ongesorteerdeLijst[R], ongesorteerdeLijst[L]
			L+=1
			R-=1
	if(Links < R): worstQuickSort(ongesorteerdeLijst, Links, R)
	if(L < Rechts): worstQuickSort(ongesorteerdeLijst, L, Rechts);
	return(ongesorteerdeLijst)

print("\n\n 2.5 \n")
minP = 0
maxP = 0
for i in range(10):
	p = 0
	random.seed()
	quickSort([random.randrange(10000) for r in range(10000)])
	#print(p, "\n")
	if (minP > p or minP == 0): minP = p
	if (maxP < p): maxP = p
print("min: {}, max: {}".format(minP, maxP))

import sys
sys.setrecursionlimit(10**4)

worstMinP = 0
worstMaxP = 0
for i in range(10):
	worstP = 0
	random.seed()
	worstList = [random.randrange(10000) for r in range(10000)]
	worstQuickSort(worstList)
	if (worstMinP > worstP or worstMinP == 0): worstMinP = worstP
	if (worstMaxP < worstP): worstMaxP = worstP
	
print("min: {}, max: {}".format(worstMinP, worstMaxP))