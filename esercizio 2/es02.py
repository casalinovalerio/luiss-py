# Per la teoria del quicksort: https://en.wikipedia.org/wiki/Quicksort
# Il qsort è un algoritmo ricorsivo per l'ordinamento di vettori.
def q_sort(vettore=[12,4,5,6,7,3,1,15]):
    minore   = []
    uguale   = []
    maggiore = []

    if len(vettore) > 1:
        pivot = vettore[0]
        for x in vettore:
            if x < pivot:
                minore.append(x)
            if x == pivot:
                uguale.append(x)
            if x > pivot:
                maggiore.append(x)
        # Chiamata ricorsiva, con il + per unire gli array
        return q_sort(minore)+uguale+q_sort(maggiore)
        
    else:  
        return array

# Il caso migliore dell'algoritmo è pari alla lunghezza del vettore (N), 
# ma il caso peggiore, che si presenta quando un vettore è ordinato nell'ordine
# inverso all'ordine richiesto, sarebbe il quadrato dello stesso. Il caso medio 
# è Nlog(N).
