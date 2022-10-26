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
        else:
            print("voor a of b in!")
    else:
        print("voor a of b in!")
        
elif antwoord == "b" or antwoord == "Karten":
    print("Hij blijft winnen maar word te oud en krijgt geen nieuw contract van formule Renault en geeft het uiteindelijk op.")
    exit()
else: print("voor a of b in!")
