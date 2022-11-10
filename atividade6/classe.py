from fruteira import Fruteira

fruta_1 = Fruteira("Banana")
fruta_2 = Fruteira ("Maça")
fruta_3 = Fruteira ("Mamão")
fruta_4 = Fruteira ("Kiwi")
fruta_5 = Fruteira("Melão")
fruta_6 = Fruteira ("Abacaxi")
fruta_7 = Fruteira ("Perá")
fruta_8 = Fruteira("Tomate")
fruta_9 = Fruteira("Abacate")
fruta_10 = Fruteira("Uva")

print("Bem-vindo a Fruteira compre bem")
cliente = input("Digite seu nome para iniciarmos: ")
print(cliente, "Temos 10 opções de frutas disponiveis : ",
"\n 0 - ", fruta_1.fruta , "\n 1 - ", fruta_2.fruta ,"\n 2 -", fruta_3.fruta ,"\n 3 -", fruta_4.fruta , "\n 4 - ", fruta_5.fruta , "\n 5 - ", fruta_6.fruta , "\n 6 - ",  fruta_7.fruta ,"\n 7 - ", fruta_8.fruta , "\n 8 - ", fruta_9.fruta ,"\n 9 - ", fruta_10.fruta)

selecao = int(input("Selecione o numero da fruta que te interressa: "))

lista_fruta = [fruta_1, fruta_2, fruta_3, fruta_4, fruta_5, fruta_6, fruta_7, fruta_8, fruta_9, fruta_10]

opcao_sel = int(selecao)

for opcao in lista_fruta:
    if opcao_sel >= 11:
        print("Essa opção de fruta nao está disponivel")
        break
    if opcao_sel <= 10:
        print(cliente, "Seu fruta escolhida foi ", lista_fruta[opcao_sel].fruta)
        print("Obrigado, volte sempre!!")
        break