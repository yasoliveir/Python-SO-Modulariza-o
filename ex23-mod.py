#Receba 3 valores obrigatoriamente em ordem crescente e um 4o valor não necessariamente em ordem. Mostre os 4 números em ordem crescente.

def ordem_cresc():
    if n4 <= n1: 
        print('Ordem crescente: ',n4, n1, n2, n3)
    elif n4 >= n1 and n4 <= n2:
        print('Ordem crescente: ',n1, n4, n2, n3)
    elif n4 >= n2 and n4 <= n3:
        print('Ordem crescente: ',n1, n2, n4, n3)
    else:
        print('Ordem crescente: ',n1, n2, n3, n4)

def main():
    global n1, n2, n3, n4
    print('---- Valores em ordem crescente ----')
    n1 = int(input('Primeiro valor: '))  
    n2 = int(input('Segundo valor: ')) 
    n3 = int(input('Terceiro valor: ')) 
    print('---- Valor não necessariamente em ordem ----')
    n4 = int(input('Quarto valor: ')) 
    print('')
    ordem_cresc()

if (__name__,'__main__'):
    main()