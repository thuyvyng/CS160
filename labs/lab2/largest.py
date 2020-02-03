bytes = input("How many bytes do you want?")
#print(bytes)
bytes = int(bytes)


#Find largest unsigned number
unsighed = 2**(bytes*8)-1
signed = 2**((bytes*8)-1)-1
smallest = 2**((bytes-1)*8)*-1
print("Smallest sighned number" + str(smallest))
print ("Largest signed number" + str(signed))
print("Largest unsigned number" + str(unsighed))
