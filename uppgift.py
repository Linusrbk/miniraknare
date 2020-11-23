inp = 0 #är variabeln som bestämmer vars man ska i miniräknaren 
resultat=0 #variabeln som ska ha det slutliga resultatet från ens uträkningar
print('välkommen till miniräknaren')#startmenyn
print('om du skriver 0 kommer du tillbaka till menyn och får ut ditt resultat')
while inp < 5:# är här så man kan komma tillbaka när man är klar med en uträkning och stänga av om det är 5 eller mer
    print('[1] räkna med +')
    print('[2] räkna med -')
    print('[3] räkna med *')
    print('[4] räkna med /')
    print('[5] avsluta')
    inp=int(input('vad vill du göra? skriv från 1 till 5:'))
    while inp == 1:#gör att om man skrev 1 kommer man hit samma med dom andra kategorierna
        plus=float(input('skriv en siffra:'))
        resultat=plus + resultat #skälva uträkningen
        if plus == 0: #gjort så man kommer tillbaka till menyn när man inte behöver något mer tal och att man får ut sitt resultat samma med dom andra kategorierna
            print(resultat)
            inp = 0

    while inp == 2:
        bastal=float(input('skriv ett bastal som ska ska minskas:'))
        minus=float(input('skriv ett tal som talet supraheras med:'))
        resultat= bastal - minus
        if minus == 0:
                print(resultat)
                inp = 0
        while inp == 2:#gjorde en till while så man inte skulle skriva bastalet om och om igen
            minus=float(input('skriv ett tal som talet supraheras med:'))
            resultat= resultat - minus
            if minus == 0:
                print(resultat) 
                inp = 0
            
    while inp == 3:
        resultat = 1 # här så man kan äns gångra för annars blir det med ett resultat som är 0 och då blir det något * 0 = 0
        while inp == 3:
            gånger=float(input('skriv en siffra:'))
            if gånger == 0: # behövde he denna förre resultatet för annars om man skrev 0 blev den slutliga resultatet alltid 0 eftersom något * 0 = 0
                print(resultat)
                inp = 0
            else:
                resultat=gånger * resultat
        
    while inp == 4:
        täljare=float(input('skriv en täljare:'))
        nämnare=float(input('skriv en nämnare:'))
        resultat= täljare / nämnare
        while inp == 4:#samma som minus så man inte skulle skriva om täljaren igen men också samma som gånger eftersom på python om man skriver något delar på 0 blir det error  
            nämnare=float(input('skriv en nämnare:'))
            if nämnare == 0: 
                print(resultat)
                inp = 0
            else:
                resultat= resultat / nämnare
print('stänger av')#ett meddelande som visar att man faktist stängt av miniräknaren