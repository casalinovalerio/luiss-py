s1 = raw_input("Inserire la stringa 1: ")
s2 = raw_input("\nInserire la stringa 2: ")
x  = int(raw_input("\nInserire il numero: "))

l1 = len(s1)

if x < l1:
	print s1[0 : x] + s2 + s1[x+1 : l1]
else:
	print "\nerrore: la lunghezza della prima stringa è: " + str(l1)
