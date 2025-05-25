import json
import os


ARQUIVO_CARDAPIO = os.path.join(os.path.dirname(__file__), 'cardapio.json')


def carregar_cardapio():
    if not os.path.exists(ARQUIVO_CARDAPIO):
        with open(ARQUIVO_CARDAPIO, 'r', encoding='utf-8') as f:
            json.dump([], f, indent=4)
    with open(ARQUIVO_CARDAPIO, 'r' , encoding='utf-8') as f:
        return json.load(f)
    
def salvar_cardapio(cardapio):
    with open(ARQUIVO_CARDAPIO, 'w', encoding='utf-8') as f:
        json.dump(cardapio, f, indent=4, ensure_ascii=False)

def adicionar_item():
    cardapio = carregar_cardapio()
    novo_item = {
        'id': len(cardapio) + 1,
        'nome': input("Nome do prato/bebida: "),
        'descricao': input("Descrição: "),
        'ingredientes': input("Ingredientes (separados por vírgula): "),
        'preco': float(input("Preço: R$ ").replace(',', '.')),
        'categoria': input("Categoria (entrada, prato principal, sobremesa, bebida): ").lower()

    }
    cardapio.append(novo_item)
    salvar_cardapio(cardapio)
    print("Item adicionado com sucesso!")        



def atualizar_item():
    cardapio = carregar_cardapio()
    id_item = int(input("Informe o ID do item que deseja atualizar: "))
    for item in cardapio:
        if item['id'] == id_item:
            print(">>>Deixei em branco para manter o valor atual<<<")
            nome = input(f"Novo nome {item['nome']}: ") or item['nome']
            descricao = input(f"Nova descrição ({item['descricao']}): ") or item['descricao']
            ingredientes = input(f"Novo ingrediente ({item['ingredientes']}): ") or item['ingredientes']
            preco_input = input(f"Novo preço ({item['preco']}): ")
            preco = float(preco_input) if preco_input else item['preco']
            categoria = input(f"Nova categoria ({item['categoria']}): ") or item['categoria']

            item.update({
                'nome': nome,
                'descricao': descricao,
                'ingredientes': ingredientes,
                'preco': preco,
                'categoria': categoria
            })
            salvar_cardapio(cardapio)
            print("Item atualizado com sucesso!")
            return
    print("Item não encontrado.")


def remover_item():
    cardapio = carregar_cardapio()
    id_item = int(input("Digite o ID do item que deseja remover: "))
    for item in cardapio:
        if item['id'] == id_item:
            cardapio.remove(item)
            salvar_cardapio(cardapio)
            print("Item removido com sucesso!")
            return