import json
import os

ARQUIVO_CARDAPIO = os.path.join(os.path.dirname(__file__), 'cardapio.json')


def carregar_cardapio():
    if not os.path.exists(ARQUIVO_CARDAPIO):
        with open(ARQUIVO_CARDAPIO, 'w', encoding='utf-8') as f:
            json.dump([], f, indent=4)
    try:
        with open(ARQUIVO_CARDAPIO, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        print("Erro ao ler o arquivo. Inicializando cardápio vazio.")
        return []


def salvar_cardapio(cardapio):
    try:
        with open(ARQUIVO_CARDAPIO, 'w', encoding='utf-8') as f:
            json.dump(cardapio, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Erro ao salvar o cardápio: {e}")


def adicionar_item():
    try:
        cardapio = carregar_cardapio()
        novo_item = {
            'id': len(cardapio) + 1,
            'nome': input("Nome do prato/bebida: ").strip(),
            'descricao': input("Descrição: ").strip(),
            'ingredientes': input("Ingredientes (separados por vírgula): ").strip(),
            'preco': float(input("Preço: R$ ").replace(',', '.')),
            'categoria': input("Categoria (entrada, prato principal, sobremesa, bebida): ").strip().lower()
        }
        cardapio.append(novo_item)
        salvar_cardapio(cardapio)
        print("Item adicionado com sucesso!")
    except ValueError:
        print("Erro: preço inválido. Use números (ex.: 10.50).")
    except Exception as e:
        print(f"Erro inesperado: {e}")


def listar_cardapio():
    try:
        cardapio = carregar_cardapio()
        if not cardapio:
            print("Cardápio vazio.")
        else:
            print("\nCARDÁPIO ATUAL:")
            for item in cardapio:
                print("-" * 40)
                print(f"ID: {item['id']}")
                print(f"Nome: {item['nome']}")
                print(f"Descrição: {item['descricao']}")
                print(f"Ingredientes: {item['ingredientes']}")
                print(f"Preço: R${item['preco']:.2f}")
                print(f"Categoria: {item['categoria']}")
    except Exception as e:
        print(f"Erro ao listar cardápio: {e}")


def filtrar_por_categoria():
    try:
        cardapio = carregar_cardapio()
        categoria = input("Digite a categoria: ").strip().lower()
        filtrados = [p for p in cardapio if p['categoria'].lower() == categoria]
        if filtrados:
            print(f"Produtos na categoria '{categoria}':")
            for p in filtrados:
                print(f"{p['nome']} - R${p['preco']:.2f}")
        else:
            print("Nenhum produto nessa categoria.")
    except Exception as e:
        print(f"Erro ao filtrar categoria: {e}")


def atualizar_item():
    cardapio = carregar_cardapio()
    while True:
        try:
            id_item = int(input("\nInforme o ID do item que deseja atualizar: ").strip())
            id_encontrado=False
            for item in cardapio:
                if item['id'] == id_item:
                    id_encontrado=True

                    nome = input(f"Novo nome ({item['nome']}): ").strip() or item['nome']
                    
                    descricao = input(f"Nova descrição ({item['descricao']}): ").strip() or item['descricao']

                    ingredientes = input(f"Novo ingrediente ({item['ingredientes']}): ").strip() or item['ingredientes']

                    preco_input = input(f"Novo preço ({item['preco']}): ").replace(',', '.').strip()
                    preco = float(preco_input) if preco_input else item['preco']

                    if preco <=0:
                        print("\nErro: O preço deve ser positivo.")
                        break
                    
                    categoria = input(f"Nova categoria ({item['categoria']}): ").strip().lower() or item['categoria']

                    
                    item.update({
                        'nome': nome,
                        'descricao': descricao,
                        'ingredientes': ingredientes,
                        'preco': preco,
                        'categoria': categoria
                    })
                    salvar_cardapio(cardapio)
                    print("\nItem atualizado com sucesso!")
                    break
            if id_encontrado==False:
                print("\nID não encontrado! Tente novamente!")

            continuar=input("\nDeseja continuar a atualização do cardápio?(s/n)").strip().lower()
            if continuar!='s':
                break     
        except ValueError:
            print("Erro: ID ou preço inválido. Tente novamente!")
        except Exception as e:
            print(f"Erro inesperado: {e}")

#FALTA AJUSTAR O DELETE!!
def remover_item():
    try:
        cardapio = carregar_cardapio()
        id_item = int(input("Digite o ID do item que deseja remover: "))
        for item in cardapio:
            if item['id'] == id_item:
                cardapio.remove(item)
                salvar_cardapio(cardapio)
                print("Item removido com sucesso!")
                return
        print("Item não encontrado.")
    except ValueError:
        print("Erro: ID inválido.")
    except Exception as e:
        print(f"Erro inesperado: {e}")
