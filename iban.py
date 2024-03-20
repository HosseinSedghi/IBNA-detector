# International Bank Account Number (IBNA) tester

from bank_codes import bank_codes
from country_codes import country_codes


iban_test1 = 'IR870570028180010653892101'

class IBNA():
	def __init__(self, number):
		self.number = number
		self.country_code = number[:2].lower()
		self.control_code = number[2:4]
		self.bank_code = number[4:7]
		self.account_type_code = number[7:8]
		self.account_code = number[8:]

	def isvalid_length(self):
		if len(self.number[2:]) == 24:
			return True
		else:
			return False

	def find_country(self):
		try:
			return country_codes[self.country_code]
		except KeyError:
			return False

	def find_bank(self):
		try:
			return bank_codes[self.bank_code]
		except KeyError:
			return False

	def is_valid(self):
		number = (int(self.number[4:] + '1827' + self.control_code)) % 97
		return True if number == 1 else False



cart = IBNA(iban_test1)

print(cart.isvalid_length())
print(cart.find_bank())
print(cart.find_country())
print(cart.is_valid())