from classe import Viagem_Tur

viagem_1 = Viagem_Tur ("Rio de Janeiro ")
viagem_2 = Viagem_Tur ("São paulo ")
viagem_3 = Viagem_Tur ("Miami ")
viagem_4 = Viagem_Tur ("Londres")
viagem_5 = Viagem_Tur ("Amsterdam ")



print("Bem-vindo!  ")
cliente = input("Digite seu nome para iniciarmos: ")
print(cliente, "Temos 5 opções de viagem: ",
"\n 1 - ", viagem_1.viagem, "\n 2 - ", viagem_2.viagem,"\n 3 -", viagem_3.viagem,"\n 4 -", viagem_4.viagem, "\n 5 - ", viagem_5.viagem)

selecao = int(input("Selecione o número do modelo que lhe interessa: "))

lista_viagem = [viagem_1, viagem_2, viagem_3, viagem_4, viagem_5]

opcao_sel = int(selecao)

for opcao in lista_viagem:
    if opcao_sel >= 5:
        print("Essa opção não está incluida no nosso pacote.")
        break
    if opcao_sel <= 4:
        print(cliente, "sua viagem escolhida foi ", lista_viagem[opcao_sel].viagem)
        print("Obrigado, volte sempre")
        break
