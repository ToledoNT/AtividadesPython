def saldo_dia (banco, titular, saldo):
    dia = {'banco': banco, 'titular': titular, 'saldo': saldo}
    return dia 

def venda (dia, valor):
    dia ['saldo'] += valor 
    
def compra (dia, valor):
    dia ['saldo'] -= valor 
    
def extrato (dia):
    print ('titular: {} \nbanco: {} \nsaldo: {}'. format(dia['titular'], dia['banco'], dia['saldo']))
    
empresadia = saldo_dia ('NUBANK', 'EMPRESA ADS', 1000.0)
venda(empresadia, 50.0)
compra (empresadia, 1000.0)
extrato (empresadia)
