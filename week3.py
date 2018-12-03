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
				#print(a)
				solutions.append(a[:])
				#print(solutions[-1])
				
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
				while current.next != None and current.next.data != e:
					current = current.next
				if current.next != None:
					current.next = current.next.next
				if current.next == None:
					print(5)
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
		if self.element > e and self.right:
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
		
#-----------------------------------------------

print("\n\n 3.3 \n")
b = BST()
for i in range(5,11):
	b.insert(i)
for i in range(6):
	b.insert(i)
print(b)
print("Maximum:", b.findMax())
print("3 in b:", b.rsearch(3)) #True
print("11 in b:", b.rsearch(11))#False
b.rinsert(11)
print("11 in b:", b.rsearch(11))#True
b.rinsert(11)
print(b)


'''
• max(self) : bereken het maximale element
• rsearch(self,e) : zoek recursief e
• rinsert(self,e) : voeg recursief e toe
• showLevelOrder(self) : toon de boom level na level. Doe dit niet recursief.
Gebruik hierbij een queue. Plaats in de queue eerst de root.
Pas de klassen 'BST' en 'BSTNode' aan. Pas alleen recursiviteit toe in 'BSTNode
'''



	