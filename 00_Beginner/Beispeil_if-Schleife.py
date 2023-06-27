# Beispiel if-Schleife
age = input("Alter des Hundes: ")
age = int(age)

if age < 0:
	print("Das stimmt wohl kaum!")
elif age == 1:
	print("entspricht ca. 14 Jahre")
elif age == 2:
	print("entspricht ca. 22 Jahre")
elif age > 2:
	human = 22 + (age -2)*5
	print("Das entspricht:", human, "Menschenjahre")

  
