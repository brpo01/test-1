Atiku = int(input("Total vote for Atiku "))
Buhari = int(input("Total vote for Buhari "))
Inconclusive = int(input("How many states were declared inconclusive? "))

if Inconclusive >= 5:
	print("The election has been cancelled")

elif(Atiku > Buhari):
	print("Atiku is Winner with %i votes" %Atiku)

elif(Atiku < Buhari):
	print("Buhari is Winner with %i votes" %Buhari)

else:
	print("The number of votes for each candidate are equal")
	statesA = int(input("How many states did Atiku win "))
	statesB = int(input("How many states did Buhari win "))
	if  (statesA + statesB) > 36:
		print("There are only 36 states in Nigeria!")

	elif statesA > statesB:
		print("Atiku is Winner")

	elif statesA < statesB:
		print("Buhari is Winner")

	else:	
		print("Re-run the election")




