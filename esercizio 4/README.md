# Esercizio 4

![es 4](testo-es4.assets/esercizio4.jpeg)

# Soluzione nel file

```python
def is_palindroma(stringa, accetta_spazi):
	
	if accetta_spazi == True:
		# Sostituzione dello spazio con carattere nullo
		stringa.replace(" ","")
	
	# Estremi della stringa vista come vettore
	l = 0
	r = len(stringa) - 1
	
	# Partendo dagli estremi, finchè non si arriva a metà
	while l < r:
		# Se anche un solo elemento non coincide, allora la stringa
		# non è palindroma, quindi return False, altrimenti controlla
		# la prossima coppia di valori
		if stringa[l] != stringa[r]:
			return False
		else:
			l = l + 1
			r = r - 1
	
	# Se non è ancora avvenuto un return False, allora la stringa è 
	# necessariamente palindroma
	return True
```

