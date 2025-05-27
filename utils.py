
import json
import os

def carregar_dados(repositorio):
    if not os.path.exists(repositorio):
        return []
    
    with open(repositorio, 'r', encoding='utf-8') as file:
        return json.load(file)

def salvar_dados(repositorio, dados):
    with open(repositorio, 'w', encoding='utf-8') as file:
        json.dump(dados, file, indent=4, ensure_ascii=False)

def adicionar_item():
    cardapio = carregar_cardapio()
    while True:
        try:
            print("\nVamos adicionar um novo item ao cardápio.")
            iniciar_insercao=input("\nPodemos começar?(s/n)").strip().lower()
            if iniciar_insercao != 's':
                print("\nVoltando para o menu cardápio...")
                break
            #Capturando os dados do novo item
            novo_item = {
                'id': len(cardapio) + 1,
                'nome': input("Nome do prato/bebida: ").strip(),
                'descricao': input("Descrição: ").strip(),
                'ingredientes': input("Ingredientes (separados por vírgula): ").strip(),
                'preco': float(input("Preço: R$ ").replace(',', '.')),
                'categoria': input("Categoria (entrada, prato principal, sobremesa, bebida): ").strip().lower()
            }
            
            # Verificar se já existe um item com determinados campos iguais no json
            if any(item['nome'].lower() == novo_item['nome'].lower() for item in cardapio):
                print(f"\nJá existe um item com o nome '{'nome'}' no cardápio.")
                continue
            elif any(item['descricao'].lower() == novo_item['descricao'].lower() for item in cardapio):
                print(f"\nJá existe um item com a mesma  '{'descricao'}' no cardápio.")
                continue

            # Verificar se todos os campos obrigatórios estão preenchidos
            elif not novo_item['nome'] or not novo_item['descricao'] or not novo_item['ingredientes'] or novo_item['preco'] <= 0 or not novo_item['categoria']:
                print("\nErro: todos os campos são obrigatórios e o preço deve ser positivo.")
                continue
                
            else:
                cardapio.append(novo_item)
                salvar_cardapio(cardapio)
                print("Item adicionado com sucesso!")
                continuar =input("\nDeseja adicionar outro item? (s/n): ").strip().lower()
                if continuar != 's':
                    print("Voltando para o menu cardápio...")
                    break
        except ValueError:
            print("Erro: preço inválido. Use números (ex.: 10,50).")
        except Exception as e:
            print(f"Erro inesperado: {e}")


