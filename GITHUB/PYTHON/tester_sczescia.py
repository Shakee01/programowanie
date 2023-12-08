##################
# TEST SZCZESCIA #
##################

import random

runda = 0

#funckja sluzaca do podania swojej odpowiedzi
def podajLiczbe():
    podaj_liczbe = int(input('podaj liczbe: '))

    if podaj_liczbe > 100:
        print('za duza liczba')
    elif podaj_liczbe < 0:
        print('za mala liczba')

x = 'y'

while x == 'y':
    liczba = random.randint(1, 100)

#poprawna odpowiedz wylosowana przez program
    def poprawnaLiczba ():
        print('poprawna odpowiedz to', liczba ) 
    podajLiczbe()

#komunikaty trafienia i nietrafienia
    if podajLiczbe == liczba:
        print('BRAWO!!! Trafiles')
        poprawnaLiczba()
        print('\n wylosowales poprawna liczne w probie ', runda, '\n' )
    else:
        print('Nie trafiles')
        poprawnaLiczba()
        runda += 1
        print('\n aktualna proba to ', runda, '\n')
#pytanie czy chcesz zagrac jeszcze raz
    x = input('Jezeli chcesz sprobowac jeszcze raz napisz y a jezeli nie napisz n: ')
    print('\n')