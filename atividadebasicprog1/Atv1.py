nome = input("Hello!! What is your name :")
print ("Welcome market Toledo", nome.title())

menu = ""
caixa = 0
receber = 0

while (menu != "s"):
	print ("Digite a opção desejada")
	print ("a. Venda - b. Receber - c. Consultar Caixa -s. Sair")
	menu = input("")
	if (menu == "a"):
		venda = float(input("Digite O valor da venda:"))
		print ("O seu caixa atual é:", caixa + venda)
		caixa = caixa + venda
	elif (menu == "b"):
                venda = float(input("Digite O valor da venda:"))
                print ("O seu caixa atual é:", caixa + venda + receber)
                caixa = caixa + venda + receber
	elif (menu == "c"):
		print("O valor em caixa é:", caixa)

	else:
		print("------------- END ----------")
		print("The system has been terminated, restart!!!")