
def cria_conta(numero, titular, saldo, limite):
    conta = {'numero':numero, 'titular':titular, 'saldo':saldo, 'limite':limite}
    return conta

def deposita(conta, valor):
        conta['saldo'] += valor
        
def saca(conta, valor):
        conta['saldo'] -= valor
        
def extrato(conta):
    print('numero : {} \nsaldo {}'.format(conta['numero1'], conta['saldo']))



conta1 = cria_conta('123-4', 'joao', 120.0, 1000.0)
conta2 = cria_conta('222', 'toledo', 100.0, 100000.0)
print(conta1)
print(conta2)


