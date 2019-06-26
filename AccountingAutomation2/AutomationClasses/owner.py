import yagmail

class Owner: 
	def __init__(self, fullName, email):
		self.fullName = fullName
		self.email = email
		self.rentals = []

	from rental import Rental

	def addRental(self, rent):
		self.rentals.append(rent)
		rent.addOwner(self)


	def sendEmail(self, fromEmail, fromEmailPassword, subject, attachments):
		yag = yagmail.SMTP(fromEmail, fromEmailPassword)
		try:
			yag.send(
			to=self.email,
			bcc=fromEmail,
			subject=subject,
			attachments=attachments)
		except:
			print('Something went wrong.')
