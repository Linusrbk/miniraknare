inp = 0
resultat=0
while inp < 5:
    print('välkommen till miniräknaren')
    print('[1] räkna med +')
    print('[2] räkna med -')
    print('[3] räkna med *')
    print('[4] valfritt arbete vet ej om jag vill ')
    print('[5] avsluta')
    print('glöm inte om du skriver 0 skippar du tillbaka till menyn')
    inp=int(input('vad vill du göra? skriv från 1 till 5:'))
    while inp == 1:
        plus=float(input('skriv en siffra:'))
        
        resultat=plus + resultat
        
        if plus == 0: 
            inp = 0
        else : 
            print(resultat)
    while inp == 2:
        print('b')
        break
    while inp == 3:
        print('b')
        break
    while inp == 4:
        print('b')
        break




print('stänger av')