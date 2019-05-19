s_letta        = ''
vocabolo       = ''
S_TERMINAZIONE = "stop"
chiave         = ''
valore         = ''
diz_IT_EN      = {}
diz_EN_IT      = {}

# Fino a che non leggiamo 'end'
while True:
	s_letta = raw_input("Inserire: <chiave>:<valore> o " +
	S_TERMINAZIONE + " per terminare!\n-> ")
	if s_letta == S_TERMINAZIONE:
		break
	
	# finchè non si vuole terminare aggiungiamo gli elementi al dizionario 
	chiave,valore = s_letta.split(":")
	diz_IT_EN[chiave] = valore
	diz_EN_IT[valore] = chiave
	
vocabolo = raw_input("\nInserire il vocabolo da ricercare: ")

# Come visto qui: https://www.tutorialspoint.com/python/python_dictionary.htm
# possiamo usare il metodo keys() per avere la lista delle chiavi
if vocabolo in diz_EN_IT.keys():
	print diz_EN_IT[ vocabolo ]

elif vocabolo in diz_IT_EN.keys():
	print diz_IT_EN[ vocabolo ]
	
else
	print "Il vocabolo non è presente nei dizionari\n"
	
