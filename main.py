'''
5.1 Feladat
Alakítsd át ezt a programot úgy, az eljárás hívásakor megadott értékpárnak megfelelően a program az adott pozícióba 'O' helyett '+' jelet írjon ki. A lenti példában az eljárás hivása: mezot_rajzol(0,4)

    O O O O + O
    O O O O O O
    O O O O O O
'''
def mezot_rajzol(x, y):
    x += 1
    szamlalo = 0
    szamlalo2 = 0
    for sor in range(3):
        szamlalo += 1
        szamlalo2 = 0
        for oszlop in range(6):
            if szamlalo == x and szamlalo2 == y:
                print('+ ', end='')
            elif szamlalo != x or szamlalo2 != y:
                print('O ', end='')
            szamlalo2 += 1
        print()


mezot_rajzol(0, 4)
