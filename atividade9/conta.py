class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print("Iniciando uma conta")
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        self.saldo -= valor

    def extrato(self):
        print('titular: {} \n saldo: {}'. format(self.titular, self.saldo))
