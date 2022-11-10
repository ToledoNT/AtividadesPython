class Email():
    def __init__(self):
        self.nome = "francis"
        self.email = "francisntoledo@hotmail.com"

    def pegar_servidor(self):
        return self.email[:14]

email = Email()
print(email.pegar_servidor())