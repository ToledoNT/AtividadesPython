from conta import Conta

contaIuri = Conta('777-4', 'IuriSantos', 150.0, 1800.0)
print(vars(contaIuri))
contaIuri.deposita(20.0)
contaIuri.extrato()
print(vars(contaIuri))