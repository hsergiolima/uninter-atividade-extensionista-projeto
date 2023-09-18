# Definição de Classes e Métodos
class Pessoa:
  def __init__(self, nome, email, telefone):
    self.nome = nome
    self.email = email
    self.telefone = telefone

class GerenciadorDePessoas:
  def __init__(self):
    self.pessoas = []

  def cadastrar_pessoa(self, nome, email, telefone):
    pessoa = Pessoa(nome, email, telefone)
    self.pessoas.append(pessoa)

  def atualizar_cadastro(self, nome, novo_email, novo_telefone):
    for pessoa in self.pessoas:
      if pessoa.nome == nome:
        pessoa.email = novo_email
        pessoa.telefone = novo_telefone
        return True
    return False

  def listar_cadastrados(self):
    return [(pessoa.nome, pessoa.email, pessoa.telefone) for pessoa in self.pessoas]

  def deletar_cadastro(self, nome):
    for pessoa in self.pessoas:
      if pessoa.nome == nome:
        self.pessoas.remove(pessoa)
        return True
    return False
# Declarações
gerenciador = GerenciadorDePessoas()

# Programa Principal
print('Bem-vindo ao Gerenciador de Voluntários!')

# Menu Principal (em loop)
while True:
  print('Entre a opção desejada:')
  opcao = int(input('1 - Cadastrar voluntário'
        '\n2 - Atualizar cadastro'
        '\n3 - Listar voluntários cadastrados'
        '\n4 - Deletar um cadastro'
        '\n0 - Sair\n'))

  # Opção 1 - Cadastrar voluntário
  if (opcao == 1):
    print('>> (1) Cadastrar voluntário <<')
    nome = input('Digite o nome: ')
    email = input('Digite o endereço de e-mail: ')
    telefone = input('Digite o telefone: ')
    gerenciador.cadastrar_pessoa(nome, email, telefone)
    print('>> Cadastro realizado com sucesso!')
    continue

  elif (opcao == 2):
    print('>> (2) Atualizar cadastro <<)')
    pessoa = input('Digite o nome do voluntário que deseja atualizar o cadastro: ')
    novo_email = input('Digite o novo endereço de e-mail: ')
    novo_telefone = input('Digite o novo telefone: ')

    if (gerenciador.atualizar_cadastro(pessoa, novo_email, novo_telefone)):
      print('>> Atualização realizada com sucesso!')
      continue
    else:
      print('>> Erro na atualização de cadastro.')
      continue

  elif (opcao == 3):
    print('>> (3) Listar cadastrados <<')
    for nome, email, telefone in gerenciador.listar_cadastrados():
      print(35*'-')
      print(f"Nome: {nome}\nEmail: {email}\nTelefone: {telefone}")
    print(35*'-')
    continue

  elif (opcao == 4):
    print('>> (4) Deletar um cadastro <<')
    pessoa_a_deletar = input('Digite o nome do voluntário')
    if gerenciador.deletar_cadastro(pessoa_a_deletar):
      print(f">> Cadastro de {pessoa_a_deletar} deletado com sucesso.")
    else:
      print(f">> Cadastro de {pessoa_a_deletar} não encontrado.")
    continue
  
  elif (opcao == 0):
    print('Encerrando o sistema.')
    break
