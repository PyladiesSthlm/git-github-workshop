class Functions:

	def __init__(self, string):
		self._string = string

	def getString(self):
		return self._string

	def setString(self, string):
		self._string = string

	def printString(self):
		print self._string

	def printLetters(self):
		for s in self._string:
			print s
