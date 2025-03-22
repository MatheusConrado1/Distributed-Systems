from Calculadora import Calculadora
from Calculadora_s import Calculadora_Science

Calculadora = Calculadora()
Calculadora_Science = Calculadora_Science()

class Despachante:
    _instancia = None

    def __new__(cls, *args, **kwargs):
        if not cls._instancia:
            cls._instancia = super(Despachante, cls).__new__(cls, *args, **kwargs)
        return cls._instancia

    def invoke(text):
        parts = text.split(',')
            
        if len(parts) < 2:
            return ("Erro: entrada mal formulada".encode('utf-8'))
        
        opp = parts[0].strip()
        
        if opp in ['+', '-', '/', '*']:
            if len(parts) == 3:
                result = Calculadora.calcular(text)
            else:
                result = "Erro: formato incorreto para operação básica"
        
        elif opp in ['^', 'sqr']:
            result = Calculadora_Science.calcular_s(text)
        
        else:
            result = "Erro: operação inválida"

        return result