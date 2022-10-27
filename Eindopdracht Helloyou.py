print ("Nate is 12 jaar en wil graag f1 racer worden, hij kart al 5 jaar en doet Europese races. En is dit jaar wereldkampion geworden. \nNu krijgt hij een contract aangeboden voor formule Renault. \nKiest hij dat contract en stijgt hij in rang of blijft hij in karten.")
print ("a - Formula Renault")
print ("b - Karten")

antwoord = input('wat kies jij? ')
if antwoord == "a" or antwoord == "Formula Renault":
    print("hij doet het erg goed en blijft winnen en word WEER wereldkampion! \nNu krijgt die de optie voor een contract verlenging en veel geld. \nOf een beginners contract in formule 4")
    
    print("a - Contract Verlenging")
    print("b - Formula 4")
    antwoord1 = input("wat kies jij? ")
    if antwoord1 == "a" or antwoord1 == "Contract Verlening":
        print("hij blijft goed presteren en bleef 2 jaar in formule Renault \nhij kreeg de optie om door te stromen naar formule 3!")
        
        print("Hij rijd erg goed en word net aan geen wereld kampioen maar wel een extra jaar in de formule 3, waar die toch wereld kampioen word, \nmaar helaas geen contract naar formule 2 omdat die geen sponsor heeft. \nBlijft hij nog een jaar in formule 3 of houd die hoop en zoekt naar sponseren? ")
        print("a - Formule 3")
        print("b - Zoeken naar sponsoren")
        antwoord3 = input("wat kies jij?")
        if antwoord3 == "a" or antwoord3 == "Formule 3":
            print("Hij blijft nog een jaar en word wereldkampioen en krijgt een Sponsor die hem helpt met zijn stoeltje voor Formule 2, \nmaar dit jaar wil helaas niemand hem aangezien het te vol is met anderen mensen met meer geld, \nNate blijft in Formule 3 voor een extra jaar om zich te bewijzen voor sponsoren en Formule 2")
            print("Nate presteert goed maar heeft het geld niet voor Formule 2, \nhij blijft in Formule 3 en word te oud voor Formule 2 en gaat hij verder in DTM. \nMisschien kan hij zich daar bewijzen.")
            print("Nate gaat fantastisch in DTM, \nword 5 keer wereld kampioen en word een Race Legende in de DTM,\nNate stopt met racen na 13 jaar in DTM en gaat met pensioen.")
            exit()
        if antwoord3 == "b" or antwoord3 == "zoeken naar sponsoren":
            print("Helaas wil niemand Nate sponsoren en is die zijn stoel in formule 3 kwijt.\nMaar hij weigert op te houden en zakt naar formule 4 terug.")
            print("Alles gaat fout voor Nate en is er helemaal klaar mee. Nate geeft op en stopt met racen voor altijd.")
            exit()
        else:
            print("voer a of b in!")

    elif antwoord1 == "b" or antwoord1 == "formula 4":
        print("Hij heeft het erg moeilijk in zijn eerste jaar en rijd niet goed maar krijgt een kans voor het jaar daarna en vind een goed momentum en wint een aantal races, \nnu krijgt die verbazingwekkend toch een contract naar formule 3!. \nMaar ook een extra contract verlening voor formule 4 op de hoop dat die zijn momentum houd.")
        print("a - Formule 4")
        print("b - Formule 3")
        antwoord2 = input("wat kies jij?")
        if antwoord2 == "a" or antwoord2 == "formule 4":
            print("Hij verliest al zijn momentum en word laten vallen door het team, helaas stopt hier de droom van Nate.")
            exit()
        if antwoord2 == "b" or antwoord2 == "formule 3":
            print("Hij doet het fantastisch en word gelijk wereld kampioen \nwaardoor die een hele goeie sponsor deal krijgt en word getekend bij het young driver program van Mercedes!. \nWaardoor die gelijk door mag naar formule 2!")
            print("Nate blijft fantastisch presenteren en blijft 2 jaar in Formule 2 en word tweevoudig wereldkampioen, \nen krijgt een Formule 1 stoel bij 2 teams. Williams (Mercedes team) of Haas ( Ferrari team) \nblijft die loyaal aan Mercedes die hem erom hebben geholpen in f2 of verraad hij Mercedes en gaat hij naar Haas.")
            print("a - Williams")
            print("b - Haas")
            antwoord4 = input("wat kies jij?")
            if antwoord4 == "a" or antwoord4 == "williams":
                print("Nate blijft loyaal aan Mercedes en zit 2 jaar bij Williams en krijgt nu de keuze om naar Aston Martin (ander Mercedes team) te gaan. \nBlijft hij bij Williams waar doe goed presteert en de auto erg goed onder controle heb. \nOf gaat hij naar Aston Martin, \neen beter team maar heeft enorme druk aangezien hij nog nooit in die auto heeft gereden.")
                
                print("a - Williams")
                print("b - Aston Martin")
                antwoord5 = input("wat kies jij?")
                if antwoord5 == 'a' or antwoord5 == 'williams':
                    print("Nate blijft bij Williams en gaat fantastisch, de auto is stuk sneller en hij pakt een paar overwinningen op, \ndit valt Mercedes op (top team) en wil Nate een stoel geven in Mercedes. \nDit is Nate zijn droom, en Williams zegt ook dat die zijn droom moet volgen. \nNate gaat naar Mercedes op zijn ultieme droom. Wereld kampioen!")
                    print("Nate rijd vanaf moment 1 fantastisch en het team blijft in hem geloven. \nNate word wereldkampioen, maar hij wil meer. \nHij wil records zetten, het team geloofd in Nate en samen gaan ze het proberen. \nHet lukt Nate om elk record te verbreken samen met Mercedes, 9 wereld titels, 123 overwinningen, 150 pole positions, 200 podiums. \nNa 13 jaar in Formule 1 in Nate tevreden en gaat hij met pensioen \nmet misschien wel de records die nooit zullen veranderen.")
                    exit()
                if antwoord5 == "b" or antwoord5 == "aston martin":
                    print("Nate heeft het lastig in Aston Martin en word gedropt, \nhij mag terug naar Williams als reserve driver, helaas blijft dit maar voor 2 jaar voordat Nate stopt met f1. \nHij krijgt een kans in Indycar (America).")
                    print("Nate Gaat erg goed in Indycar en wint een paar titels, tot het helemaal fout gaat en overlijd nadat zijn auto in brand vliegt tijdens een pit probleem met de brandstof.")
                    exit()
                else:
                    print("voer a of b!")
            if antwoord4 == "b" or antwoord4 == "haas":
                print("Niet verbazend was Mercedes woest op Nate en hebben zijn contract verbroken. \nToch presteert Nate erg goed in de Haas, \nnu buiten alle verwachtingen krijgt Nate een contract van Ferrari zelf! Gaat hij naar het Top team \nof blijft hij bij Haas en hoopt dat het team beter blijft gaan en misschien samen met Haas wereld kampioen kan worden.")
                print("a - Haas")
                print("b - Ferrari")
                antwoord6 = input("wat kies jij")
                if antwoord6 == "a" or antwoord6 == "haas":
                    print("Nate Blijft bij Haas en het team word het beste team op de grid, \nhij wint het wereldkampioenschap 3 keer met Haas en besluit te stoppen met racen na 5 jaar, \nhij heeft zijn droom gehaald.")
                    exit()
                if antwoord6 == "b" or antwoord6 == "Ferrari":
                    print("Na een goed jaar met Ferrari met 2 overwinningen en 9 podiums blijft hij bij Ferrari, tot het fout gaat. Tijdens een erg natte race in Japan verliest Nate controle over zijn auto, maakt een zware crash en overlijd later in het ziekenhuis.")
                    exit()
            else:
                print("voer a of b in!")
        else:
            print("voer a of b in!")
    else:
        print("voer a of b in!")
        
elif antwoord == "b" or antwoord == "Karten":
    print("Hij blijft winnen maar word te oud en krijgt geen nieuw contract van formule Renault en geeft het uiteindelijk op.")
    exit()
else: print("voer a of b in!")
