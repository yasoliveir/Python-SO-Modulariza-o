 #Receba 2 valores inteiros. Calcule e mostre o resultado da diferença do maior pelo menor valor.
dif = 0
n1 = 0
n2 = 0
menor = 0
maior = 0

def diferenca():
    global dif, maior, menor, n1, n2
    if n1 > n2:
        maior = n1
        menor = n2
    else:
        maior = n2
        menor = n1
    dif = maior - menor
    print('A diferença entre o maior e o menor número é:', dif)

def main():
    global n1, n2
    n1 = int(input('Primeiro número: '))
    n2 = int(input('Segundo número: '))
    diferenca()

if (__name__== '__main__'):
    main()
