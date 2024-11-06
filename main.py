##sistema de gerenciamento de estoque

class produto:
  def __init__(self, id, nome, categoria_id, quantidade, preço):
    self.id = id
    self.nome = nome
    self.categoria_id = categoria_id
    self.quantidade = quantidade
    self.preço = preço

class categoria:
  def __init__(self, id, nome):
    self.id = id
    self.nome = nome

class movimentação:
  def __init__(self, id, produto_id, quantidade, tipo_movimentação, data):
    self.id = id
    self.produto_id = produto_id
    self.quantidade = quantidade
    self.tipo_movimentação = tipo_movimentação
    self.data = data

def cadastrar_produtos(produtos, contador_produtos):
  id = contador_produtos + 1
  nome = input("Digite o nome do produto: ")
  categoria_id = int(input("Digite o ID da categoria do produto: "))
  quantidade = int(input("Digite a quantidade do produto: "))
  preço = float(input("Digite o preço do produto: "))
  produtos.append(produto(id, nome, categoria_id, quantidade, preço))
  print("produto cadastrado com sucesso!")
  return contador_produtos + 1

def consultar_produto_id(produtos, id):
  for produto in produtos:
    if produto.id == id:
      print(f'ID: {produto.id}, nome: {produto.nome}, categoria: {produto.categoria_id}, quantidade: {produto.quantidade}, preço: {produto.preço}')
      return

  print("produto não encontrado!")
##teste cadastro
produtos = []
Contador = 0

Contador = cadastrar_produtos(produtos, Contador)

consultar_produto_id(produtos, Contador)                                                                