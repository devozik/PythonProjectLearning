from random import randint

while True:
    try:
        z1 = int(input('Podaj początek losowania: '))
        z2 = int(input('Podaj koniec losowania: '))
        break
    except ValueError:
        print('Liczbę...')
        continue

ran = randint(z1, z2)
proby = []
while True:
    try:
        wybor = int(input(f'Podaj liczbę od {z1} do {z2}: '))
        if z1 <= wybor <= z2:
            while wybor != ran:
                print('Niestety to nie to')
                wybor = int(input(f'Podaj liczbę od {z1} do {z2}: '))
                proby.append(wybor)
            else:
                proby.append(wybor)
                print(f'Brawo trafiłeś za {len(proby)} razem!')
                print(f'Wylosowana liczba to {ran}.')
            break
        else:
            print(f'Miała być liczba w zakresie {z1} do {z2}')
    except ValueError:
        print('Liczbę...')
