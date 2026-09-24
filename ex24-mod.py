#Receba um valor inteiro. Verifique e mostre se é divisível por 2 e 3.
def divisivel():
    
    if (x % 2 == 0) and (x % 3 == 0):
        print(f'O número {x} é divisível por 2 e 3')
    elif (x % 2 == 0) and (x % 3 != 0):
        print(f'O número {x} é divisível apenas por 2')
    elif (x % 2 != 0) and (x % 3 == 0):
        print(f'O número {x} é divisível apenas por 3')
    else:
        print('O número não é divisível nem por 2 nem por 3')

def main():
    global x
    x = int(input('Valor inteiro: '))
    divisivel()


if (__name__, '__main__'):
    main()