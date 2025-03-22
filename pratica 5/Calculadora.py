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
