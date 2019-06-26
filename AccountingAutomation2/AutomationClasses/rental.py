

class Rental:
	def __init__(self, nickname, address, rate):
		self.nickname = nickname
		self.address = address
		self.rate = rate
		self.owner = []
		self.statements = []
	
	def addOwner(self, ownerObj):
		self.owner.append(ownerObj)

	from statement import Statement

	def addStatement(self, statementObj):
		self.statements.append(statementObj)
		statementObj.addRentalOwnership(self)

