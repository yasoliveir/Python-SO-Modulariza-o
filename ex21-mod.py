'''Receba 4 notas bimestrais de um aluno. Calcule e mostre a média aritmética. Mostre a mensagem de acordo com a média:
a. Se a média for >= 6,0 exibir “APROVADO”;
b. Se a média for >= 3,0 E < 6,0 exibir “EXAME”;
c. Se a média for < 3,0 exibir “RETIDO'''

def media_aluno():
    global n1, n2, n3, n4
    media = (n1 + n2 + n3 + n4) / 4
    if media >= 6:
        print(f"""Média: {media}
    Situação: A P R O V A D O""")
    elif media >= 3 and media < 6:
        print(f"""Média: {media} 
    Situação: E X A M E""")
    else:
        print(f"""Média: {media}
    Situação: R E T I D O""")

def main():
    global n1, n2, n3, n4
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    n3 = float(input('Nota 3: '))
    n4 = float(input('Nota 4: '))
    media_aluno()

if (__name__== '__main__'):
    main()