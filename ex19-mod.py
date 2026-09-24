#Receba 2 valores reais. Calcule e mostre o maior deles.

v1 = 0
v2 = 0
maior = 0
menor = 0

def calculo_maior():
    global v1, v2, maior, menor
    if v1 > v2:
        maior = v1
        menor = v2
    else:
        maior = v2
        menor = v1
    print('O maior entre os números é:', maior)

def main():
    global v1, v2
    v1 = float(input('Primeiro número: '))
    v2 = float(input('Segundo número: '))
    calculo_maior()
if (__name__== '__main__'):
    main()