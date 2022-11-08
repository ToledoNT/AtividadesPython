from classe import Agenda

contato_1 = Agenda ("Vanley - 7185748930")
contato_2 = Agenda ("yuri - 81783781")
contato_3 = Agenda ("Ana Julia - 81718237")
contato_4 = Agenda ("Joao Victor - 1892789")
contato_5 = Agenda ("Elieser - 71723838")
contato_6 = Agenda ( "l - 781781")


print("Bem-vindo a Biblioteca Hacking On")
cliente = input("Digite seu nome para iniciarmos: ")
print(cliente, "Temos 10 opções de livros disponiveis : ",
"\n 0 - ", contato_1.contato, "\n 1 - ", contato_2.contato,"\n 2 -", contato_3.contato,"\n 3 -", contato_4.contato, "\n 4 - ", contato_5.contato ,"\n 5 - ", contato_6.contato )

selecao = int(input("Selecione o numero do contato que te interressa: "))

lista_contato = [contato_1, contato_2, contato_3, contato_4, contato_5, contato_6]

opcao_sel = int(selecao)

for opcao in lista_contato:
    if opcao_sel >= 6:
        print("Essa opção não está disponivel")
        break
    if opcao_sel <= 5 :
        print(cliente, "Contato escolhido foi: ", lista_contato[opcao_sel].contato)
        print("Obrigado, volte sempre!!")
        break

