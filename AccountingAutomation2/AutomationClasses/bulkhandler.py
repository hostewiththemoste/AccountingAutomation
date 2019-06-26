import re
from owner import Owner
from rental import Rental

class BulkHandler:
	def __init__(self, ownerList = [], rentalList = [], statementList = []):
		self.ownerList = ownerList
		self.rentalList = rentalList
		self.statementList = statementList
		
	def getOwnerData(self, fileName):
		f = open(fileName, 'r')
		for line in f:
			splitLine = re.split('[|]', line)
			fullName = splitLine[0]
			email = splitLine[1]
			newOwner = Owner(fullName.strip(), email.strip())
			self.ownerList.append(newOwner)

	def getRentalData(self, fileName):
		f = open(fileName, 'r')
		for line in f:
			splitLine = re.split('[|]', line)
			nickname = splitLine[0]
			address = splitLine[1]
			rate = 0.20
			newRental = Rental(nickname.strip(), address.strip(), rate)
			self.rentalList.append(newRental)

	def setOwnerships(self, fileName):
		f = open(fileName, 'r')
		for line in f:
			splitLine = re.split('[|]', line)
			ownerName = splitLine[1].strip()
			rentalName = splitLine[0].strip()
			for owner in self.ownerList:
				if owner.fullName == ownerName:
					for rental in self.rentalList:
						if rental.nickname == rentalName:
							owner.addRental(rental)
						else:
							pass
				else: 
					pass


