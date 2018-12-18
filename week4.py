'''
———————————————————————————————————————————————
GITHUB --> https://github.com/Dwarf-Nebula/alds
———————————————————————————————————————————————

1720840
TICT_V1C / TCTI-V2ALDS1
'''
#4.1
print("\n\n4.1\n")
from random import uniform
class SCH:
	def __init__(self, tableSize):
		self.tableSize = tableSize
		self.table = []
		for i in range(self.tableSize):
			self.table.append([])
		self.nElements = 0
		
	def __str__(self):
		tmpString = ""
		for elements in self.table:
			tmpString+="-"
			for element in elements:
				tmpString += str(element) + ", "
			tmpString+="\n"
		tmpString += "Loadfactor is {}%\n".format(self.nElements/self.tableSize*100)
		return tmpString
		
	def search(self, e):
		if e in self.table[hash(e)%self.tableSize]:
				return True
		return False
		
	def insert(self, e):
		if self.search(e):
			return False
		self.nElements += 1
		if self.nElements/self.tableSize > 0.75:
			self.rehash(self.tableSize*2)
		self.table[hash(e)%self.tableSize].append(e)
		return True
		
	def delete(self, e):
		if e in self.table[hash(e)%self.tableSize]:
			self.table[hash(e)%self.tableSize].remove(e)
			return True
		return False
		
	def rehash(self, newLen):
		tmp = [] * newLen
		self.tableSize = newLen
		for i in range(self.tableSize):
			tmp.append([])
		for elements in self.table:
			for e in elements:
				tmp[hash(e)%self.tableSize].append(e)
		self.table = tmp

hashtable = SCH(10)
for x in range(200):
	if hashtable.insert(round(uniform(0, 1), 3)):
		continue
	else:
		while not hashtable.insert(round(uniform(0, 1), 3)):
			continue

for x in range(100):
	if hashtable.delete(round(uniform(0, 1), 3)):
		continue
	else:
		while not hashtable.delete(round(uniform(0, 1), 3)):
			continue
	
print(hashtable)

print("\n\n4.2\n")

def twoFloatsSameHash():
	d = {}
	twoPower32 = 2**32
	while True:
		floatX = uniform(0, 1)
		hashX = hash(floatX) % (twoPower32)
		if hashX in d:
			print("{} and {} have the same hashvalue: {}".format(repr(d[hashX]), repr(floatX), hashX))
			return d[hashX], floatX, hashX
		d[hashX] = floatX
		
twoFloatsSameHash()

print("\n\n4.3\n")

def b(n, k):
	assert(n >= k)
	outputList = [[1]]
	while len(outputList) <= n:
		outputList.append([1])
		for i in range(0, len(outputList[-2])-1):
			outputList[-1].append(outputList[-2][i]+outputList[-2][i+1])
		outputList[-1].append(1)
	return outputList[n][k]

print(b(6, 3))
print(b(100, 50))

print("\n\n4.4\n")

def f(amount): #amount is euro
	amount = int(amount * 100)
	coins = [1,2,5,10,20,50,100,200,500,1000,2000,5000,10000]
	waysOfPaying = [[1]*(amount+1)]
	amountOfCoins = len(coins)
	for i in range(1, amountOfCoins):
		for j in range(amount+1):
			if j == 0:
				waysOfPaying.append([1])
			elif j >= coins[i] :
				waysOfPaying[i].append(waysOfPaying[i-1][j] + waysOfPaying[i][j-coins[i]])
			elif j < coins[i] :
				waysOfPaying[i].append(waysOfPaying[i-1][j])
	return waysOfPaying[-1][amount]

print(f(0.07))