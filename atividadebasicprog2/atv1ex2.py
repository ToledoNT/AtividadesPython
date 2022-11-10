EX 1: 
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


>>>>>>-------------------------------------------------------------------------------------------------------------------------<<<<<<
EX 2:
def cria_conta(numero, titular, saldo, limite):
    conta= {'numero': numero, 'titular': titular, 'saldo': saldo, 'limite':limite}
    return conta
    
def deposita(conta, valor):
    conta ['saldo'] += valor

def saque(conta, valor):
    conta ['saldo'] -= valor
    
def extrato(conta):
    print('numero: {}'. format(conta['numero']), conta['saldo'])
contaVanley = cria_conta ('123-4', 'Vanley', 150.0, 1000.0)
deposita (contaVanley, 200.0)
extrato (contaVanley)



