'''
———————————————————————————————————————————————
GITHUB --> https://github.com/Dwarf-Nebula/alds
———————————————————————————————————————————————

Jasper van Poelgeest
1720840
TICT_V1C / TCTI-V2ALDS1
Frits Dannenberg
'''

#1.1
"""
Berekend de maximale waarde van een lijst met ints en/of floats

Parameters
----------
lijst : list
De list met ints en floats

Return
------
newMax: int of float
de maximale waarde in de lijst
"""
def myMax(lijst):
		assert len(lijst)
		newMax = lijst[0]
		for item in lijst:
				assert ((type(item) == int) or (type(item) == float))
				if (item > newMax):
						newMax = item
		return newMax

print(myMax([2, 1, 5, 2.1, 19.4, 10, 8, 3, 1]))

#1.2
"""
Returnt een lijst met alle nummers in een string.

Parameters
----------
zin : string
Dit is de string waar de nummers uit gehaald gaan worden

Return
------
returnlist: list
Dit is een list met integers die in de zin zaten
"""
def getNumbers(zin):
		assert (type(zin) == str)
		returnlist = []
		tempstring = ""
		for letter in zin:
				if (letter >= "0" and letter <= "9"):
						tempstring += letter
				else:
						if (tempstring != ""):
								returnlist.append(int(tempstring))
								tempstring = ""
		return returnlist

print(getNumbers('een123zin45 6met-632meerdere+7777getallen'))

#1.3
"""
Berekend de priemgetallen tot aan n

Parameters
----------
n : int
De waarde tot waar de priemgetallen worden berekend

Return
------
primes: list
List met priemgetallen
"""
def calcPrime(n):
		assert (type(n) == int)
		numbers = []
		primes = []
		for i in range(n+1):
				numbers.append(True)
		p = 2
		while (p * p <= n):
				if (numbers[p] == True):
						for i in range(p * 2, n+1, p): 
								numbers[i] = False
				p += 1
		for i in range(2, n):
				if (numbers[i]):
						primes.append(i)
		return primes

print(calcPrime(1000))

#1.4
"""
Berekend de kans dat in een groep 2 mensen op dezelfde dag jarig zijn.
Parameters
----------
nGroepen : int
Aantal groepen

groepGrootte : int
De grootte van de groepen

Return
------
counter/nGroepen: float
Het aantal getelde groepen met 2+ personen die op dezelfde dag jarig zijn gedeeld door de hoeveelheid groepen.
"""
import random
def chanceTwoPeopleSameBirthday(nGroepen, groepGrootte):
		assert(type(nGroepen) == int and type(groepGrootte) == int)
		randomNumbers = []
		counter = 0
		for i in range(nGroepen):
				randomNumbers.append([])
				for j in range(groepGrootte):
						randomNumbers[i].append(random.randrange(365))
				for j in range(365):
						if (randomNumbers[i].count(j) > 1):
								counter+=1
								break
		return counter/nGroepen
		
print(chanceTwoPeopleSameBirthday(100, 57))