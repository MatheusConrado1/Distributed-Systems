def soma(a, b):
    result = a + b
    return result


def subtracao(a, b):
    result = a - b
    return result

def multiplicacao(a, b):
    result = a * b
    return result

def divisao(a, b):
    try:
        b != 0
        result = a / b
        return result
    except ValueError:
        error = "Nao foi possivel realizar a operacao"
    return error

def calcular(text):
    opp, op_1, op_2 = text.split(',')
    op1 = float(op_1)
    op2 = float(op_2)

    if opp == '+': result = soma(op1, op2)
    elif opp == '-': result = subtracao(op1, op2)
    elif opp == '*': result = multiplicacao(op1, op2)
    elif opp == '/': result = divisao(op1, op2)
    
    else: result = "Sentença mal formulada"

    return result