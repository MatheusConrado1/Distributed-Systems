import math

class Calculadora_Science:
    _instancia = None

    def __new__(cls, *args, **kwargs):
        if not cls._instancia:
            cls._instancia = super(Calculadora_Science, cls).__new__(cls, *args, **kwargs)
        return cls._instancia

    def __init__(self):
        print("Calculadora cientifica criada")

    def sqr_root(self, a):
        result = math.sqrt(a)
        return result

    def power_n(self, a, n):
        result = pow(a, n)
        return result

    def calcular_s(self, text):
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

        if opp == 'sqr': result = self.sqr_root(op1)
        elif opp == '^': result = self.power_n(op1, op2)
        else: result = "Sentença mal formulada"

        return result

