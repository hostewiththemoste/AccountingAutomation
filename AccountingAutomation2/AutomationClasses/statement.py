import os

class Statement:
	def __init__(self, month, year, fileName, nickname):
		self.month = month
		self.year = year
		self.fileName = fileName
		self.nickname = nickname
		self.rentalOwnership = ''
	
	def displayOnScreen(self, fileName):
		os.startfile(fileName)

	def addRentalOwnership(self, rent):
		self.rentalOwnership = rent
import os

class Statement:
	def __init__(self, month, year, fileName, nickname):
		self.month = month
		self.year = year
		self.fileName = fileName
		self.nickname = nickname
		self.rentalOwnership = ''
	
	def displayOnScreen(self, fileName):
		os.startfile(fileName)

	def addRentalOwnership(self, rent):
		self.rentalOwnership = rent
