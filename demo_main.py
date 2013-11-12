from functions import Functions

def main():
	
	original_string = "Hello world!"

	# Create an object f of type Functions. Internal f.__string is set to original_string at initialization
	f = Functions(original_string)

	
	# If the internal variable f.__string has been changed, we check if it was changed using the setter f.setString()
	if f.getString() != original_string and f.setterUsed() == False:
		print "ERROR! Something is wrong here! Did you manipulate private variables in the Functions class directly??"
		# Hint: We didn't, there is a bug in the Functions class	
	else:
		f.printString() # Print out f.__string	


if __name__ == "__main__":
    main()
