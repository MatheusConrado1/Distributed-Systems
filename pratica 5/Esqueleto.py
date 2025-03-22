from Calculadora import Calculadora
from Calculadora_s import Calculadora_Science

class Esqueleto:
    _instancia = None

    def __new__(cls, *args, **kwargs):
        if not cls._instancia:
            cls._instancia = super(Esqueleto, cls).__new__(cls, *args, **kwargs)
        return cls._instancia

    def calcular(self, text):
        try:
            opp, op_1, op_2 = text.split(',')
            op1 = float(op_1)
            op2 = float(op_2)

            if opp == '+':
                return Calculadora.soma(op1, op2)
            elif opp == '-':
                return Calculadora.subtracao(op1, op2)
            elif opp == '*':
                return Calculadora.multiplicacao(op1, op2)
            elif opp == '/':
                return Calculadora.divisao(op1, op2)
            else:
                return "Sentença mal formulada"
        except ValueError:
            return "Erro ao processar entrada. Certifique-se de usar o formato correto: operador,op1,op2"