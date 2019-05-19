l1  = raw_input("Inserire gli elementi separati da uno spazio:\n")
l2  = []
tmp = 0
n   = int(raw_input("\nInserire n: "))
m   = int(raw_input("\nInserire m: "))

# divide gli elementi separati da uno spazio e li inverte
lista = lista.split(" ").reverse()

# calcolo la lunghezza di l1
lun1 = len(l1)

l2 = l1

if n < len1 and m < len1:
	# scambio dei valori all'indice m ed n (se possibile)
	tmp   = l2[m]
	l2[m] = l2[n]
	l2[n] = tmp
	
# unisce gli elementi in una stringa: 
# https://www.tutorialspoint.com/python/string_join.htm
print "L1 = " + " ".join(l1) + "\nL2 = " + " ".join(l2)
