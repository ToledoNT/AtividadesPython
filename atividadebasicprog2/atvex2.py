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
