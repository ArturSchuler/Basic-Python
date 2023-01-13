# primeiro teste


peso = float(input('Qual seu peso?: '))
altura = float(input('Qual sua altura?: '))


def x(peso, altura):
    try:
        peso/(altura**2)
    except (TypeError, ValueError):
        print('acontedeu um erro de tipagem')
    except ZeroDivisionError:
        print('não é possivel dividir um numero por zero')
    except Exception as erro:
        print(f'o erro encontrado foi {erro.__class__}')
    else:
        print('Voce mede {} metros e pesa {} kg.'.format(altura, peso))
    return x


def imc():
    if x <= 30:
        return str('Seu IMC está ok')
    else:
        return str('Seu IMC indica obesidade')
    
