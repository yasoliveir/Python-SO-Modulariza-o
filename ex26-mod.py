#Receba 2 números inteiros. Verifique e mostre se o maior número é múltiplo do menor.

def multiplos():
    global x1, x2, maior, menor, divisao
    if x1 > x2:
        maior = x1
        menor = x2
        divisao = maior // menor
        if maior % menor == 0:
            print(f'{maior} é divisível por {menor}\nO resultado da divisão é {divisao}')
        else:
            print(f'{maior} não é divisível por {menor}') 
    elif x2 > x1:
        maior = x2
        menor = x1
        divisao = maior // menor
        if maior % menor == 0:
                print(f'{maior} é divisível por {menor}\nO resultado da divisão é {divisao}')
        else:
            print(f'{maior} não é divisível por {menor}') 
    else:
        print(f'Número iguais, portanto o {x1} é divisível por {x2}\nO resultado da divisão é 1')

def main():
    global x1, x2
    x1 = int(input('Primeiro Número: '))
    x2 = int(input('Segundo Número: '))
    multiplos()

if (__name__,'__main__'):
    main()