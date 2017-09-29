# Collatz Conjecture
def collatz(n):
	# Hash table for intermediate values 
	intermediate = [None] * 10000 # Fill the hash table with nulls
	file = open("intermediate.txt", "w")

	nValue = str("Value of n: " + str(n) + "\n") # Puts the value of n into a string
	print(nValue, end = ""); # Prints the value of n to console
	file.write(nValue) # Writes the value of n to the text file

	for i in range(n,0,-1): # Go from integer n to 1
		x = i; # The current intermediate value
		iteration = str("x = " + str(x) + ":")

		print(iteration, end = "") # Print the iteration number

		# Run the loop while the intermediate value does not equal 1 
		#(Terminates when it reaches 1) or the value has been previously
		# hashed into the intermediate list
		# Don't need to test for 1 because the first run of the function will
		# yield a 1 at the end
		while (x != 1) and (intermediate[x] is None): 
			intermediate[x] = x # Hash x into the xth element of the hash table
			print (intermediate[x], end = " ") # Print the values
			iteration = str(iteration + str(intermediate[x]) + " ") # Concatenate the string with the value

			if (x % 2 == 0): # If x is even
				x = int(x / 2) # Set the next term
			else:
				x = int(x * 3 + 1) # Set the next term

		iteration = str(iteration + "\n") # Add a new line to the string
		print() # Print new line to console
		file.write(iteration) # Write the numbers generated in the iteration to a text file
	file.close()

n = 100
collatz(n) # Sample output with n = 100