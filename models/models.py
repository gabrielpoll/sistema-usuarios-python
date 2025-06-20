import json

class Usuario:
    def __init__(self, nome_completo, idade, email, cpf):
        self.__nome_completo = nome_completo
        self.__idade = idade
        self.__email = email
        self.__cpf = cpf

    @property
    def nome(self):
        return self.__nome_completo

    @nome.setter
    def nome(self, receber_nome):
        self.__nome_completo = receber_nome

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, receber_idade):
        self.__idade = receber_idade

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, receber_email):
        self.__email = receber_email

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, receber_cpf):
        self.__cpf = receber_cpf

    def to_dict(self):
        return {
            "nome": self.nome,
            "idade": self.idade,
            "email": self.email,
            "cpf": self.cpf
        }


class Sistema:
    def __init__(self):
        self.usuarios = []
        self.carregar_arquivo()

    def cadastrar_usuario(self):
        nome = input("Nome completo: ")
        idade = int(input('Idade: '))
        email = input("Email: ")
        cpf = int(input("CPF: "))

        for u in self.usuarios:
            if u.cpf == cpf:
                print("CPF já cadastrado")
                return
        novo = Usuario(nome.title(), idade, email, cpf)
        self.usuarios.append(novo)
        print("Usuario cadastrado com sucesso")

    def listar_usuarios(self):
        if not self.usuarios:
            print("Nenhum usuario encontrado!")
        else:
            for u in self.usuarios:
                print(f'Nome: {u.nome} | Idade: {u.idade} | Email: {u.email} | CPF: {u.cpf}')

    def buscar_usuario(self):
        cpf = int(input("Qual o CPF do usuario? "))
        for u in self.usuarios:
            if u.cpf == cpf:
                print("Usuario encontrado")
                print(f'Nome: {u.nome} | Idade: {u.idade} | Email: {u.email} | CPF: {u.cpf}')
                return
        print("Usuario não localizado")

    def remover_usuario(self):
        cpf = int(input("Digite o CPF do usuario que deseja excluir: "))
        for i, u in enumerate(self.usuarios):
            if u.cpf == cpf:
                print("Apagando usuario")
                del self.usuarios[i]
                return
        print("Usuario não existe")

    def salvar_em_arquivo(self, nome_arquivo="usuarios.json"):
        with open(nome_arquivo, 'w') as arquivo:
            lista_dicts = [usuario.to_dict() for usuario in self.usuarios]
            json.dump(lista_dicts, arquivo, indent=4)

    def carregar_arquivo(self, nome_arquivo="usuarios.json"):
        try:
            with open(nome_arquivo, 'r') as arquivo:
                lista_dicts = json.load(arquivo)
                self.usuarios = [Usuario(d["nome"], d["idade"], d["email"], d["cpf"]) for d in lista_dicts]


        except FileNotFoundError:
            self.usuarios = []






