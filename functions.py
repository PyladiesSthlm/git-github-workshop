class Functions:

	# Initializer that sets two 'private' internal variables
	def __init__(self, string):
		self.__string = string # Internal variable self.__string is set to input parameter
		self.__setterUsed = False # Internal variable self.__setterUsed checks if setter was used to set self.__string

	# Returns self.__string
	def getString(self):
		return # BUG!! Should return self.__string
	
	# Returns True if setString() has been called, False otherwise
	def setterUsed(self):
		return self.__setterUsed
	
	# Sets self.__string without manipulating it directly
	def setString(self, string):
		self.__setterUsed = True
		self.__string = string

	# Prints out self.__string
	def printString(self):
		print self.__string
