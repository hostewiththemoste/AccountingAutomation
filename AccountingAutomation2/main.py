from bulkhandler import BulkHandler

allList = BulkHandler()

allList.getOwnerData('data/ownerData.txt')

allList.getRentalData('data/rentalData.txt')

allList.setOwnerships('data/rentalOwners.txt')



for owner in allList.ownerList:
	print(owner.fullName + ': ')
	for rental in owner.rentals:
		print(rental.nickname)
		print(' ' + str(rental.rate))
	print('\n')

	print("hello world")