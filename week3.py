'''
———————————————————————————————————————————————
GITHUB --> https://github.com/Dwarf-Nebula/alds
———————————————————————————————————————————————

1720840
TICT_V1C / TCTI-V2ALDS1
'''
#3.1

def check(a,i): # ga na of i aan a toegevoegd kan worden
	n = len(a)
	return not (i in a or # niet in dezelfde kolom
	i+n in [a[j]+j for j in range(n)] or # niet op dezelfde diagonaal
	i-n in [a[j]-j for j in range(n)]) # niet op dezelfde diagonaal


def printQueens(solutionArray):
	for solution in solutionArray:
		n = len(solution)
		for i in range(n):
			for j in range(n):
				if solution[i] == j: print("X", end = " ")
				else: print("*", end = " ")
			print()
		print()

def research(N):
	global a
	global solutions
	for i in range(N):
		if check(a,i):
			a.append(i)
			if len(a) == N:
				solutions.append(a[:])		
			else:
				if research(N):
					continue
			del a[-1] # verwijder laatste element
	return False

print("\n\n 3.1 \n")
solutions = []
a = []
research(8)
printQueens(solutions)
print("Aantal oplossingen:", len(solutions))

#3.2
class ListNode:
	def __init__(self,data,next_node):
		self.data = data
		self.next = next_node
	def __repr__(self):
		return str(self.data)

class MyCircularLinkedList:
	def __init__(self):
		self.tail = None
	
	def __repr__(self):
		s = ''
		current = self.tail
		if current == None:
			return 'empty list'
		current = current.next
		s += str(current)
		current = current.next
		while current != self.tail.next:
			s += " -> " + str(current)
			current = current.next
		return s

	def append(self,e):
		if not self.tail:
			self.tail = ListNode(e, None)
			self.tail.next = self.tail
		else:
			n = ListNode(e, self.tail.next)
			self.tail.next = n
			self.tail = self.tail.next

	def delete(self,e):
		if self.tail:
			if self.tail.data == e:
				if self.tail.next == self.tail:
					self.tail = None
				else:
					self.tail = self.tail.next
			else:
				current = self.tail.next
				while current.next != self.tail.next and current.next.data != e:
					current = current.next
				if current.next.data != e:
					return False
				if current.next != self.tail:
					current.next = current.next.next
				if current.next == self.tail:
					self.tail = current

print("\n\n 3.2 \n")
mylist =  MyCircularLinkedList()
print(mylist)
mylist.append(1)
print(mylist)
mylist.append(2)
print(mylist)
mylist.append(3)
mylist.append(5)
mylist.append(4)
print(mylist)
mylist.delete(2)
print(mylist)
mylist.delete(1)
print(mylist)
mylist.delete(3)
print(mylist)

#3.3
import math

class BSTNode:
	def __init__(self,element,left,right):
		self.element = element
		self.left = left
		self.right = right

	def __repr__(self,nspaces=0):
		s1 = ''
		s2 = ''
		s3 = ''
		if self.right != None:
			s1 = self.right.__repr__(nspaces + 3)
		s2 = s2 + ' '*nspaces + str(self.element) + '\n'
		if self.left != None:
			s3 = self.left.__repr__(nspaces + 3)
		return s1 + s2 + s3

	def insert(self,e):
		parent = self
		current = None
		found = False

		if parent.element < e:
			current = parent.right
		elif parent.element > e:
			current = parent.left
		else:
			found = True;

		while not found and current:
			parent = current
			if parent.element < e:
				current = parent.right
			elif parent.element > e:
				current = parent.left
			else:
				found = True

		if not found:
			if parent.element < e:
				parent.right = BSTNode(e,None,None)
			else:
				parent.left = BSTNode(e,None,None)
		return not found

	def insertArray(self,a, low=0, high=-1):
		if len(a) == 0:
			return
		if high == -1:
			high = len(a)-1
		mid = (low+high+1)//2
		self.insert(a[mid])
		if mid > low:
			self.insertArray(a,low,mid-1)
		if high > mid:
			self.insertArray(a,mid + 1,high)

	def search(self,e):
		current = self
		found = False
		while not found and current:
			if current.element < e:
				current = current.right
			elif current.element > e:
				current = current.left
			else:
				found = True
		if found:
			return current
		else:
			return None

	def search2(self,e):
		if self.element == e:
			return self
		parent = self.getParent(e)
		if parent == None:
			return None
		if parent.element < e:
			return parent.right
		return parent.left

	def getParent(self,e):
		parent = self
		current = None
		found = False

		if parent.element < e:
			current = parent.right
		elif parent.element > e:
			current = parent.left;
		else:
			return None

		while not found and current:
			if current.element == e:
				found = True
			else:
				parent = current
				if current.element < e:
					current = current.right
				else:
					current = current.left
		if found:
			return parent
		else:
			return None

	def parentMinRightTree(self):
		parent = self.right
		current = parent.left
		while current.left:
			parent = current
			current = current.left
		return parent

	def delete(self,e):
		parent = self.getParent(e);

		if parent == None:
			return False
		if parent.element < e:
			current = parent.right
			if current.left == None:
				parent.right = parent.right.right
				return True
			else:
				if current.right == None:
					parent.right = parent.right.left
					return True
		else:
			current = parent.left
			if current.left == None:
				parent.left = parent.left.right
				return True
			else:
				if current.right == None:
					parent.left = parent.left.left
					return True
		if current.right.left == None:
			current.element = current.right.element
			current.right = current.right.right
			return True
		node = current.parentMinRightTree()
		current.element = node.left.element
		node.left = node.left.right
		return True

#-----------------------------------------------

	def rsearch(self, e):
		if self.element == e:
			return True
		if self.element < e and self.right:
			return self.right.rsearch(e)
		if self.element > e and self.left:
			return self.left.rsearch(e)
		return False
	
	def rinsert(self, e):
		if self.element == e:
			return
		
		if self.element < e and self.right:
			self.right.rinsert(e)
		elif self.element < e and not self.right:
			self.right = BSTNode(e,None,None)
		
		elif self.element > e and self.right:
			return self.left.rinsert(e)
		elif self.element > e and not self.left:
			self.left = BSTNode(e,None,None)
		return False
	
#-----------------------------------------------

class BST:
	def __init__(self,a=None):
		if a:
			mid = len(a)//2
			self.root = BSTNode(a[mid],None,None)
			self.root.insertArray(a[:mid])
			self.root.insertArray(a[mid+1:])
		else:
			self.root = None

	def __repr__(self):
		if self.root:
			return str(self.root)
		else:
			return 'null-tree'

	def search(self,e):
		if self.root and e:
			return self.root.search(e)
		else:
			return None

	def insert(self,e):
		if e:
			if self.root:
				return self.root.insert(e)
			else:
				self.root = BSTNode(e,None,None)
				return True
		else:
			return False

	def delete(self,e):
		if self.root and e:
			if self.root.element == e:
				if self.root.left == None:
					self.root = self.root.right
				elif self.root.right == None:
					self.root = self.root.left
				elif self.root.right.left == None:
					self.root.element = self.root.right.element
					self.root.right = self.root.right.right
				else:
					node = self.root.parentMinRightTree();
					self.root.element = node.left.element
					node.left = node.left.right
					return True
			else:
				return self.root.delete(e)
		else:
			return False
		
#-----------------------------------------------

	def findMax(self):
		maxValue = self.root.element
		current = self.root
		while(current.right):
			if (current.right.element > maxValue):
				maxValue = current.right.element
			current = current.right
		return maxValue
	
	def rsearch(self, e):
		return self.root.rsearch(e)
	
	def rinsert(self, e):
		self.root.rinsert(e)
	
	def showLevelOrder(self):
		nodesToDo = [self.root]
		nodesSeen = []
		nodeIndex = 0
		while nodesToDo:
			if all(node is None for node in nodesToDo[nodeIndex:]):
				break
			nodesSeen.append(nodesToDo[nodeIndex])

			if nodesToDo[nodeIndex]:
				if nodesToDo[nodeIndex].left != None:
					nodesToDo.append(nodesToDo[nodeIndex].left)
				else:
					nodesToDo.append(None)

				if nodesToDo[nodeIndex].right != None:
					nodesToDo.append(nodesToDo[nodeIndex].right)
				else:
					nodesToDo.append(None)
			else:
				nodesToDo.append(None)
				nodesToDo.append(None)
			nodeIndex+=1
		levelSize = 0
		maxLevelSize = 1
		levelDepth = 0
		outputNodes = [[]]
		for node in nodesSeen:
			try:
				outputNodes[levelDepth].append(node.element)
			except:
				outputNodes[levelDepth].append("N")
			levelSize+=1
			if levelSize == maxLevelSize:
				maxLevelSize *= 2
				outputNodes.append([])
				levelSize = 0
				levelDepth += 1
		
		if not len(outputNodes[-1]): outputNodes.pop()
		while levelSize < maxLevelSize and levelSize != 0:
			outputNodes[levelDepth].append("N")
			levelSize+=1

		width = len(outputNodes[-1])
		
		levelCounter = 1
		for nodes in outputNodes:
			spaces = int(width/levelCounter)-1
			print(" "*spaces, end = "")
			for node in nodes:
				print(node, end=" "*((spaces*2)+1))
			print()
			levelCounter*=2
		
#-----------------------------------------------

print("\n\n 3.3 \n")
b = BST()
for i in range(7, 10):
	b.insert(i)
for i in range(7):
	b.insert(i)
print(b)
print("Maximum:", b.findMax())
print("3 in b:", b.rsearch(3)) #True
print("10 in b:", b.rsearch(10))#False
b.rinsert(10)
print("10 in b:", b.rsearch(10))#True
b.rinsert(10)
print(b)
b.showLevelOrder()


#3.4
import csv
def calcWordFreq(file):
	assert(type(file) == str)
	words = fileToList(file)
	if words != False:
		wordFreq = {}
		for word in words:
			if word in wordFreq:
				wordFreq[word]+=1
			else:
				wordFreq[word] = 1
		return wordFreq
	return False

def fileToList(fileString):
	try:
		file = open(fileString, "r")
		lines = file.read().splitlines()
		words = []
		for line in lines:
			tmp = line.split(" ")
			for word in tmp:
				words.append(word)
		file.close()
		return words
	except:
		print("Couldn't open file")
		return False

def dictToCSV(dictionary):
	with open('counted_words.csv', mode='w') as countedWordFile:
		countedWordWriter = csv.writer(countedWordFile, delimiter=',')
		countedWordWriter.writerow(["Word", "Frequency"])
		for key in dictionary:
			countedWordWriter.writerow([key, dictionary[key]])
		countedWordFile.close()
	
print("\n\n 3.3 Dictionary\n")
dictToCSV(calcWordFreq("randomtekst.txt"))

class trieNode:
	def __init__(self):
		self.freq = 0
		self.chars = {}
	
	def insert(self, key, value):
		if key in self.chars:
			if len(value) < 1:
				self.chars[key].freq +=1
			else:
				self.chars[key].insert(key+value[0], value[1:])
		else:
			if len(value) < 1:
				self.chars[key] = trieNode()
				self.chars[key].freq +=1
			else:
				self.chars[key] = trieNode()
				self.chars[key].insert(key+value[0], value[1:])
	
	def writeFrequencyToFile(self, csvWriter):
		for key in self.chars:
			if self.chars[key].freq > 0:
				csvWriter.writerow([key, self.chars[key].freq])
			self.chars[key].writeFrequencyToFile(csvWriter)
	
	
class trie:
	def __init__(self):
		self.root = trieNode()
	
	def insert(self, value):
		self.root.insert(value[0], value[1:])
		
	def writeFrequencyToFile(self, outputFileName):
		assert(type(outputFileName) == str)
		with open(outputFileName, mode='w') as countedWordFile:
			countedWordWriter = csv.writer(countedWordFile, delimiter=',')
			countedWordWriter.writerow(["Word", "Frequency"])
			
			for key in self.root.chars:
				if self.root.chars[key].freq > 0:
					countedWordWriter.writerow([key, self.root.chars[key].freq])
				self.root.chars[key].writeFrequencyToFile(countedWordWriter)
	
	def inputFile(self, fileString):
		try:
			file = open(fileString, "r")
			lines = file.read().splitlines()
			for line in lines:
				tmp = line.split(" ")
				for word in tmp:
					self.root.insert(word[0], word[1:])
			file.close()
		except:
			print("Couldn't open file")
			return False
	
print("\n\n 3.3 Trie\n")
boom = trie()

boom.inputFile("randomtekst.txt")
boom.writeFrequencyToFile("counted_words2.csv")
