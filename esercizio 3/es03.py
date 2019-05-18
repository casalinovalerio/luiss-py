# Funzione che ritorna il minimo tra a e b
def minimo(a, b):
	return a if (b > a) else b

# Funzione ricorsiva
def vett_min(vettore, l, r):
	if r - l <= 1:
		return minimo(vettore[l], vettore[r]) 
	else:
		return minimo( 
		vett_min(vettore, l, r/2), 
		vett_min(vettore, r/2 + 1, r) 
		)
	
# Inizializzo con valori qualsiasi
vettore = [2,3,1,5]

# Printiamo il risultato
print str(vett_min(vettore, 0, len(vettore)-1))
