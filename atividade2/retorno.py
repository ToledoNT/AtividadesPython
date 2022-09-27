def cria_conta(al, user, entrada, nivel):
    conta = {'al': al, 'user': user, 'entrada': entrada, 'nivel': nivel}
    return conta

def ca(conta, valor):
    conta['entrada'] += valor

def controle(conta, valor):
    if (conta['entrada'] < valor):
        print('Valor Invalido')
    else:
        conta['entrada'] -= valor
        return True
    
def upentrada(conta, valor):
    conta['nivel'] += valor

def ext(conta):
    print('Conta\n Matricula:',conta['al'], '\n  user:',conta['user'], '\n  taxa:',conta['entrada'], '\n    nivel:',conta['nivel'])

contaFT = cria_conta('9999-1', 'Toledo', 2000, 8)
controle(contaFT, 500.0)
upentrada(contaFT, 5)
ext(contaFT)
