# definizione delle variabili
area          = 0
data          = 0
base          = 0
altezza       = 0
lato          = 0
usr_input     = ''
DEF_TRIANGOLO = 't'
DEF_QUADRATO  = 'q'

usr_input = raw_input(DEF_TRIANGOLO + " per triangolo\n" +
                  DEF_QUADRATO + " per quadrato\nInput: ")

if usr_input == DEF_TRIANGOLO:
    data = raw_input("digita: <base> <altezza>\nInput: ")

    # In base salvo la prima parte della stringa, in altezza salvo la seconda
    # parte. La prima e la seconda parte vengono determinate dal
    # separatore " ", ovvero lo spazio. Guida:
    # https://www.pythonforbeginners.com/dictionary/python-split
    base,altezza = data.split(" ")

    # converto in intero
    base    = int(base)
    altezza = int(altezza)

    print "Output: " + str(base*altezza/2) + "\n"

elif usr_input == DEF_QUADRATO:
    data = raw_input("digita: <lato>\nInput: ")

    # converto in intero
    lato    = int(data)

    print "Output: " + str(lato*lato) + "\n"

else:
    
    print "Opzione" + usr_input + "non valida"
