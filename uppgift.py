inp = 0
resultat=0
while inp < 5:
    print('välkommen till miniräknaren')
    print('[1] räkna med +')
    print('[2] räkna med -')
    print('[3] räkna med *')
    print('[4] valfritt arbete vet ej om jag vill ')
    print('[5] avsluta')
    print('om du skriver 0 skippar du tillbaka till menyn och får ut ditt resultat')
    inp=int(input('vad vill du göra? skriv från 1 till 5:'))
    while inp == 1:
        plus=float(input('skriv en siffra:'))
        
        resultat=plus + resultat
        
        if plus == 0: 
            print(resultat)
            inp = 0

    while inp == 2:
        bastal=float(input('skriv ett bastal som ska ska minskas:'))
        minus=float(input('skriv en supraherare:'))
        resultat= bastal - minus
        if minus == 0:
                print(resultat)
                inp = 0
        while inp == 2:
            minus=float(input('skriv en supraherare:'))
            resultat= resultat - minus
            if minus == 0:
                print(resultat) 
                inp = 0
            
            
    while inp == 3:
        print('b')
        break
    while inp == 4:
        print('b')
        break




print('stänger av')