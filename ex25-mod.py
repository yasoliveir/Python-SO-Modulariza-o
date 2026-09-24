#Receba a hora de início e de final de um jogo (HH,MM), calcular o tempo do jogo em horas e minutos, sabendo que o tempo máximo é menor que 24 horas e pode começar num dia e terminar noutro.

def duracao_jogo():
    global inicio_em_minutos, h_fim, h_inicio, m_fim, m_inicio, fim_em_minutos, duracao_total, horas, minutos
    inicio_em_minutos = h_inicio * 60 + m_inicio
    fim_em_minutos = h_fim * 60 + m_fim

    if fim_em_minutos <= inicio_em_minutos:
        fim_em_minutos += 24 * 60  # 1440 minutos (24 horas)

    duracao_total = fim_em_minutos - inicio_em_minutos
    # Converte min p horas
    horas = duracao_total // 60
    minutos = duracao_total % 60
    print (f'O jogo teve duração de {horas} horas e {minutos} minutos')

# Cálculo e exibição do resultado
def main():
    global inicio_em_minutos, h_fim, h_inicio, m_fim, m_inicio, fim_em_minutos, duracao_total, horas, minutos
    h_inicio = int(input('Hora de Inicio (HH): '))
    m_inicio = int(input('Minuto de Inicio (MM): '))
    h_fim = int(input('Hora de Término (HH): '))
    m_fim = int(input('Minuto de Término (MM): '))
    duracao_jogo()

if (__name__, '__main__'):
    main()
# def tempo_jogo():
#     from datetime import datetime
#     global dt, dt2
#     dt = datetime.datetime.strptime(h1, "%H:%M")
#     dt2 = datetime.datetime.strptime(h2, "%H:%M")
#     print(dt2)

# def main():
#     global h1, h2
#     h1 = input('Hora de início (HH:MM): ')
#     h2 = input('Hora de Término (HH:MM): ')
#     tempo_jogo()

# if (__name__, '__main__'):
#     main()


