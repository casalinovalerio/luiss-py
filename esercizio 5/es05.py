# Acquisizione da tastiera del numero n
n = int(raw_input("Inserire un numero: "))
i = 0

# Per definizione un numero primo è divisibile solo per 1 e per se stesso,
# quindi il resto della divisione intera per qualsiasi altro numero dovrebbe 
# essere diverso da 0
for i in range (2, n - 1):
	if n % i == 0:
		return False
		
# Non è stato smentito che fosse un numero primo
return True
