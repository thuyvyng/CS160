def labs():
	labq = int(input(" How many labs do you have? "))
	labs = 0
	for x in range(labq):
		labg = int(input("What did you get on each lab?(out of 10) "))
		labs = labs + labg
	labcent = labs / (10*labq)
	labcc = labcent *25	
	print(labcc)
	return labcc

def assignments():
	assq = int(input("How many assignments do you have ?"))
	ass = 0
	for x in range(assq):
		assg = int(input( "What did you get on each assignment?(out of a 100) "))
		ass = ass + assg
	asscent = ass / (100*assq)
	asscc = asscent * 65
	print(asscc)
	return asscc

def part():
	partq = int(input("What is your participation grades? (out of 100)"))
	partcc = partq/10
	print(partcc)
	return partcc

def main():
	final = labs() + assignments() + part()
	print(final)



main()




"""questlab = int(input("How many labs do you have? "))
labs = 0
for x in range(questlab):
	labgrades = int(input(" What percentage did you get on each lab? "))
	labs = labs + labgrades
print(labs*.25)


partquestion = int(input(" What is your participation percentage grade?" ))

questassign = int(input("How many assignments do you have? "))
quests = 0
for x in range(questassign):
	assigngrades = int(input("What percent did you get on each assignment? "))
	quests = quests + assigngrades

finalgrade = (labs*.25) + (partquestion*.1) + (quests*.65)

print(finalgrade)

"""
