import math

def sqr_root(a):
    result = math.sqrt(a)
    return result

def power_n(a, n):
    result = pow(a, n)
    return result

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

