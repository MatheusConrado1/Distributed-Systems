import math

def sqr_root(a):
    try:
        result = math.sqrt(a)
        return result
    except ValueError:
        error = "Deu n kkkkkk"
        return error
    


def power_n(a, n):
    try:
        result = pow(a, n)
        return result
    except ValueError:
        error = "Deu n kkkkkk"
        return error

def calcular_s(text):
    parts = text.split(',')
    if len(parts) == 2:
        opp, op_1 = parts
        op1 = float(op_1)
        op2 = None
    elif len(parts) == 3:
        opp, op_1, op_2 = parts
        op1 = float(op_1)
        op2 = float(op_2)
    else:
        return "Sentença mal formulada"

    if opp == 'sqr': result = sqr_root(op1)
    elif opp == '^': result = power_n(op1, op2)
    else: result = "Sentença mal formulada"

    return result

