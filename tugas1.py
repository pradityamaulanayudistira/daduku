import random


def roll(sides=6):
    lempardadu = random.randint(1, sides)
    return lempardadu


def main():
    putar = True
    while putar:
        userbertanya = str(
            input('\n Apakah anda ingin bermain dadu? [yes/no]'))
        if userbertanya.lower() != 'no':
            dadu = roll()
            print('Angka yang keluar: ', dadu)
        else:
            putar = False
    print('\n Terimakasih Sudah Bermain')


main()
