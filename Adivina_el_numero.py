import random


def run():
    numero_random = random.randint(1,100)
    numero_elegido = int(input('ingresa un numero del 1 al 100: '))
    while numero_random != numero_elegido:
        if numero_elegido < numero_random:
            print('busca un numero mas grande')
        else:
            print('busca un numero mas pequeño')
        numero_elegido = int(input("elije otro numero: "))
    print('GANASTE')


if __name__ == "__main__":
    run()