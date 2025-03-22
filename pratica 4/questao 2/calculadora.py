class Calculadora:
    _instancia = None

    def __new__(cls, *args, **kwargs):
        if not cls._instancia:
            cls._instancia = super(Calculadora, cls).__new__(cls, *args, **kwargs)
        return cls._instancia

    def __init__(self):
        print("Calculadora criada")

    def soma(self, a, b):
        return a + b

    def subtracao(self, a, b):
        return a - b

    def multiplicacao(self, a, b):
        return a * b

    def divisao(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Não foi possível realizar a operação: divisão por zero"

    def calcular(self, text):
        try:
            opp, op_1, op_2 = text.split(',')
            op1 = float(op_1)
            op2 = float(op_2)

            if opp == '+':
                return self.soma(op1, op2)
            elif opp == '-':
                return self.subtracao(op1, op2)
            elif opp == '*':
                return self.multiplicacao(op1, op2)
            elif opp == '/':
                return self.divisao(op1, op2)
            else:
                return "Sentença mal formulada"
        except ValueError:
            return "Erro ao processar entrada. Certifique-se de usar o formato correto: operador,op1,op2"
