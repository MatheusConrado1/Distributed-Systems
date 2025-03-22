from TCPClient import Client

class ProxyCalc:
    _instancia = None

    def __new__(cls, *args, **kwargs):
        if not cls._instancia:
            cls._instancia = super(ProxyCalc, cls).__new__(cls, *args, **kwargs)
        return cls._instancia
    
    def __init__(self):
        print("ProxyCalc criado")

    def soma(self, op1, op2):  
        return f'+,{op1},{op2}'

    def subtracao(self, op1, op2):  
        return f'-,{op1},{op2}'

    def multiplicacao(self, op1, op2):  
        return f'*,{op1},{op2}'

    def divisao(self, op1, op2):  
        return f'/,{op1},{op2}'
    
    def treat_response(self, text):
        client = Client()
        req = None

        try:
            opp, op_1, op_2 = text.split(',')
            op1 = float(op_1)
            op2 = float(op_2)
            if opp in ['+', '-', '/', '*']:
                if opp == '+': req = self.soma(op1, op2)
                elif opp == '-': req = self.subtracao(op1, op2)
                elif opp == '*': req = self.multiplicacao(op1, op2)
                elif opp == '/': req = self.divisao(op1, op2)
        except Exception as e:
            print(f"Erro: {e}")

        if req : client.sendReq(req)
