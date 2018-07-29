#-*- coding: utf-8 -*-
import random
#Just adding a random comment

def intToFootNukeCoch(randResult):
    """Funktio muuntaa annetun kokonaisluvun (0-2) merkkijonoksi"""
    if randResult == 0:
        return "Jalka"
    elif randResult == 1:
        return "Ydinase"
    else:
        return "Torakka"

def footNukeCochToInt(userInput):
    """Funktio muuntaa annetun merkkijonon (J,Y,T) kokonaisluvuksi"""
    if userInput == "Jalka":
        return 0
    elif userInput == "Ydinase":
        return 1
    else:
        return 2

def greater(ansPlay, ansComp):
    """Vertailee kumpi annetuista parametreistä on suurempi ja palauttaa 1 (ansPlay > ansComp) 1 (ansPlay < ansComp) tai 0"""
    if ansPlay > ansComp:
        return 1
    elif ansPlay < ansComp:
        return 2
    else:
        return 0

def main():
    roundCount = 0
    playWinCount = 0
    tieCount = 0
    while True:
        answer = input("Jalka, Ydinase vai Torakka? (Lopeta lopettaa): ")
        if answer == "Lopeta":
            print("Pelasit",roundCount,"kierrosta, joista voitit",playWinCount,"ja pelasit tasan",tieCount,"peliä.")
            break
        else:
            roundCount += 1
            playAns = footNukeCochToInt(answer)
            compAns = random.randint(0,2)
            result = greater(playAns, compAns)
            print("Sinä valitsit: ",answer,"\ntietokone valitsi: ",intToFootNukeCoch(compAns),compAns)

            if playAns < compAns:
                print("Hävisit!")
            elif playAns > compAns:
                playWinCount += 1
                print("Voitit!")
            else:
                tieCount += 1
                print("Tasapeli!")

if __name__ == "__main__":
    main()
#And some more comments to the end
