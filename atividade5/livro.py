from classe import Biblioteca

livro_1 = Biblioteca ("Pentest em Aplicação Web")
livro_2 = Biblioteca ("Tecnicas de Invasão de Sistemas")
livro_3 = Biblioteca ("Pentest em Rede de Computadores")
livro_4 = Biblioteca ("Pentest em Redes sem Fios")
livro_5 = Biblioteca ("Testes de Invasão")
livro_6 = Biblioteca ( "Manual do Hacker")
livro_7 = Biblioteca ("Introdução ao Hacking")
livro_8 = Biblioteca ("Web Segura")
livro_9 = Biblioteca ("Avaliação de segurança de redes")
livro_10 = Biblioteca ("Google Hacking para pentest")

print("Bem-vindo a Biblioteca Hacking On")
cliente = input("Digite seu nome para iniciarmos: ")
print(cliente, "Temos 10 opções de livros disponiveis : ",
"\n 1 - ", livro_1.livro, "\n 2 - ", livro_2.livro,"\n 3 -", livro_3.livro,"\n 4 -", livro_4.livro, "\n 5 - ", livro_5.livro ,"\n 6 - ", livro_6.livro ,"\n 7 - ", livro_7.livro ,"\n 8 - ", livro_8.livro , "\n 9 - ", livro_9.livro ,"\n 10 - ", livro_10.livro)

selecao = int(input("Selecione o numero do livro que te interressa: "))

lista_livro = [livro_1, livro_2, livro_3, livro_4, livro_5, livro_6, livro_7, livro_8, livro_9, livro_10]

opcao_sel = int(selecao)

for opcao in lista_livro:
    if opcao_sel >= 11:
        print("Essa opção não está disponivel")
        break
    if opcao_sel <= 10:
        print(cliente, "Seu livro escolhido foi ", lista_livro[opcao_sel].livro)
        print("Obrigado, volte sempre!!")
        break

