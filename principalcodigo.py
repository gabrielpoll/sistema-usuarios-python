from models.models import Usuario, Sistema

def rodar_usuarios():
   sistema = Sistema()
   while True:
       menu()
       resposta = int(input())
       if resposta == 1:
           sistema.cadastrar_usuario()
       elif resposta == 2:
           sistema.listar_usuarios()
       elif resposta == 3:
           sistema.buscar_usuario()
       elif resposta == 4:
           sistema.remover_usuario()
       elif resposta == 5:
           sistema.salvar_em_arquivo()
           print("Salvando...")
           print("Sistema salvo e fechado com sucesso")
           break
       else:
           print("Por favor, selecione uma opção válida.")

def menu():
    print('------ Menu ------')
    print('1. Cadastrar novo usuario')
    print('2. Listar usuários')
    print('3. Buscar usuário por CPF')
    print('4. Excluir usuario')
    print('5. Sair')
    print('--------------------------')

if __name__ == '__main__':
    rodar_usuarios()
