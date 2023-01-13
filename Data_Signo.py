
def retornaMes(mes):  # converte o mes numero na str.
    meses = ['', 'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
             'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    return meses[mes]


def l():
    print('-' * 30)


def iniciar():
    nome = str(input('Qual seu nome?: '))
    dia = int(input('Que dia você nasceu?: '))
    mes = int(input('Qual mês você nasceu?: '))
    ano = int(input('Qual ano você nasceu?: '))
    dataNasc = '{} de {} de {}'.format(
        dia, retornaMes(mes), ano)
    print('Seja bem vindo {}, você nasceu em {}.'.format(nome, dataNasc))
    l()
    return dia, mes, nome


st = str('Seu signo solar é')


def retornaSigno(dia, mes):
    Signos = {1: 'Aries', 2: 'Touro', 3: 'Gemeos', 4: 'cancer', 5: 'Leão',
              6: 'Virgem', 7: 'Libra', 8: 'Escorpião', 9: 'Sagitario', 10: 'Capricornio', 11: 'Aquario', 12: 'Peixes'}
    if (dia >= 21 & mes == 1) | (dia <= 19 & mes == 2):
        return Signos[11]
    elif (dia >= 19 & mes == 2) | (dia <= 20 & mes == 3):
        return Signos[12]
    elif (dia >= 21 & mes == 3) | (dia <= 20 & mes == 4):
        return Signos[1]
    elif (dia >= 21 and mes == 4) or (dia <= 20 and mes == 5):
        return Signos[2]
    elif (dia >= 21 and mes == 5) or (dia <= 20 and mes == 6):
        return Signos[3]
    elif (dia >= 21 and mes == 6) or (dia <= 22 and mes == 7):
        return Signos[4]
    elif (dia >= 23 and mes == 7) or (dia <= 22 and mes == 8):
        return Signos[5]
    elif (dia >= 23 and mes == 8) or (dia <= 22 and mes == 9):
        return Signos[6]
    elif (dia >= 23 and mes == 9) or (dia <= 22 and mes == 10):
        return Signos[7]
    elif (dia >= 23 and mes == 10) or (dia <= 21 and mes == 11):
        return Signos[8]
    elif (dia >= 22 and mes == 11) or (dia <= 21 and mes == 12):
        return Signos[9]
    elif (dia >= 22 and mes == 12) or (dia <= 20 and mes == 1):
        return Signos[10]


def retorna(dia, mes):
    print(st, retornaSigno(dia, mes))
    l()
    return retornaSigno(dia, mes)

# Áries: 21 de março a 20 de abril
# Touro: 21 de abril a 20 de maio
# Gêmeos: 21 de maio a 20 de junho
# Câncer: 21 de junho a 22 de julho
# Leão: 23 de julho a 22 de agosto
# Virgem: 23 de agosto a 22 de setembro
# Libra: 23 de setembro a 22 de outubro
# Escorpião: 23 de outubro a 21 de novembro
# Sagitário: 22 de novembro a 21 de dezembro
# Capricórnio: 22 de dezembro a 20 de janeiro
# Aquário: 21 de janeiro a 19 de fevereiro
# Peixes: 19 de fevereiro a 20 de março
