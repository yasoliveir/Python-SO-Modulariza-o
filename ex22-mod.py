#Receba 2 valores inteiros e diferentes. Mostre seus valores em ordem crescente.

def ordem_cresc():
    global x1, x2
    if x1 < x2:
        print(f'Ordem crescente dos números: {x1} | {x2}')
    elif x1 > x2:
        print(f'Ordem crescente dos números: {x2} | {x1}')
    else:
        print('Os números são iguais')

def main():
    global x1, x2
    x1 = int(input('Primeiro Número Inteiro: '))
    x2 = int(input('Segundo Número Inteiro: '))
    ordem_cresc()

if (__name__, '__main__'):
    main()