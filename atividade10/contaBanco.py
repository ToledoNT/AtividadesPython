def cria_conta(numero, titular, saldo, limite):
    conta = {'numero': numero, 'titular': titular, 'saldo': saldo, 'limite': limite}
    return conta

def deposita(conta, valor):
    conta['saldo'] += valor

def saca(conta, valor):
    conta['saldo'] -= valor

def extrato(conta):
    print('numero: {}'. format(conta['numero']), conta['saldo'])

contaIuri = cria_conta('777-4', 'Iuri', 150.0, 1000.0)
deposita(contaIuri, 200.0)
extrato(contaIuri)