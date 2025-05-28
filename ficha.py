import json
import os

ARQUIVO_FICHAS = 'ficha.json'

def carregar_fichas():
    try:
        with open(ARQUIVO_FICHAS, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Arquivo inválido ou não encontrado. Criando novo...")
        with open(ARQUIVO_FICHAS, 'w') as f:
            json.dump([], f)
        return []

def salvar_fichas(fichas):
    with open(ARQUIVO_FICHAS, 'w') as f:
        json.dump(fichas, f, indent=4)

def adicionar_ficha(fichas):
     while True:
        print("\n" + "=" * 40)
        print("ADICIONAR NOVA FICHA".center(40))
        print("=" * 40)

        while True:
            nome = input("Nome: ").strip().capitalize()
            if not nome:
                print("Nome não pode ser vazio!")
                continue
        
            nome_existe = any(f['nome'].lower() == nome.lower() for f in fichas)
            if nome_existe:
                print("Já existe uma ficha com este nome!")
            else:
                break
        
        while True:
            categoria = input("Categoria: ").strip().upper()
            if categoria:
                break
            print("Categoria não pode ser vazia!")

        ingredientes = []
        print("\nINGREDIENTES:")
        while True:
            ingred = input("Ingrediente (deixe em branco para parar): ").capitalize()
            if not ingred:
                if not ingredientes:
                    print("Adicione pelo menos 1 ingrediente!")
                    continue
                break

            quant = input("Quantidade: ").strip()
            while not quant:
                print("Quantidade não pode ser vazia!")
                quant = input("Quantidade: ").strip()
                
            ingredientes.append({'ingrediente': ingred, 'quantidade': quant})
        
        preparo = []
        print("\nMODO DE PREPARO:")
        passo_num = 1
        while True:
            descricao = input(f"Passo {passo_num} (deixe em branco para parar): ").strip().capitalize()
            if not descricao:
                if not preparo:
                    print("Adicione pelo menos 1 passo!")
                    continue
                break
            preparo.append({'passo': passo_num, 'descricao': descricao})
            passo_num += 1
    
        nova_ficha = {
            'categoria': categoria,
            'nome': nome,
            'ingredientes': ingredientes,
            'preparo': preparo
        }

        fichas.append(nova_ficha)
        salvar_fichas(fichas)
        print("\nFicha adicionada com sucesso!")

        op = input("\nAdicionar outra ficha? (s/n): ").lower()
        if op != 's':
            break


def visualizar_fichas(fichas):
    if not fichas:
        print("\nNenhuma ficha cadastrada ainda!")
        input("Pressione Enter para voltar...")
        return
    
    categorias = sorted(set(f['categoria'] for f in fichas))

    for categoria in categorias:
        print("\n" + "=" * 90)
        print(f"\n{categoria.upper():^90}")
        print("=" * 90)

        fichas_cat = [f for f in fichas if f['categoria'] == categoria]
        for ficha in  fichas_cat:
            
            print(f"Nome: {ficha['nome']}")
        
            print("\nIngredientes:")
            for ingred in ficha['ingredientes']:
                print(f"- {ingred['quantidade']} de {ingred['ingrediente']}")
        
            print("\nModo de Preparo:")
            for passo in ficha['preparo']:
                print(f"{passo['passo']}. {passo['descricao']}")
                print("-" * 90)
        
    input("\nPressione Enter para voltar...")

def editar_fichas(fichas):
    if not fichas:
        print("\nNenhuma ficha cadastrada para editar!")
        input("Pressione Enter para voltar...")
        return

    while True:
        print("\n" + "=" * 40)
        print("EDITAR FICHA".center(40))
        print("=" * 40)

        for i, ficha in enumerate(fichas, 1):
            print(f"{i}. {ficha['nome']} ({ficha['categoria']})")

        try:
            escolha = int(input("\nDigite o número da ficha que deseja editar: "))
            if escolha < 1 or escolha > len(fichas):
                print("Opção inválida!")
                continue
        except ValueError:
            print("Entrada inválida!")
            continue

        ficha_encontrada = fichas[escolha - 1]

        print(f"\nEditando ficha: {ficha_encontrada['nome']}")
        print(f"Categoria: {ficha_encontrada['categoria']}")
        print("\nIngredientes:")
        for i in ficha_encontrada['ingredientes']:
            print(f"- {i['quantidade']} de {i['ingrediente']}")
        print("\nModo de Preparo:")
        for p in ficha_encontrada['preparo']:
            print(f"{p['passo']}. {p['descricao']}")
        print("-" * 40)

        novo_nome = input(f"Novo nome (deixe em branco para manter o atual) [{ficha_encontrada['nome']}]: ").strip().capitalize()
        if novo_nome:
            nome_existe = any(f['nome'].lower() == novo_nome.lower() and f != ficha_encontrada for f in fichas)
            if nome_existe:
                print("Já existe outra ficha com este nome!")
            else:
                ficha_encontrada['nome'] = novo_nome

        nova_categoria = input(f"Nova categoria (deixe em branco para manter a atual) [{ficha_encontrada['categoria']}]: ").strip().upper()
        if nova_categoria:
            ficha_encontrada['categoria'] = nova_categoria

        if input("\nEditar ingredientes? (s/n): ").lower() == 's':
            novos_ingredientes = []
            print("\nNovos ingredientes:")
            while True:
                ingred = input("Ingrediente (deixe em branco para parar): ").strip().capitalize()
                if not ingred:
                    if not novos_ingredientes:
                        print("Erro: A ficha precisa ter pelo menos 1 ingrediente!")
                        continue
                    break
                quant = input("Quantidade: ").strip()
                while not quant:
                    print("Quantidade não pode ser vazia!")
                    quant = input("Quantidade: ").strip()
                novos_ingredientes.append({'ingrediente': ingred, 'quantidade': quant})

            ficha_encontrada['ingredientes'] = novos_ingredientes

        if input("\nEditar modo de preparo? (s/n): ").lower() == 's':
            novo_preparo = []
            print("\nNovo modo de preparo:")
            passo_num = 1
            while True:
                descricao = input(f"Passo {passo_num} (deixe em branco para parar): ").strip().capitalize()
                if not descricao:
                    if not novo_preparo:
                        print("Adicione pelo menos 1 passo!")
                        continue
                    break
                novo_preparo.append({'passo': passo_num, 'descricao': descricao})
                passo_num += 1

            ficha_encontrada['preparo'] = novo_preparo

        salvar_fichas(fichas)
        print("\nFicha atualizada com sucesso!")

        if input("\nEditar outra ficha? (s/n): ").lower() != 's':
            break

def excluir_fichas(fichas):
    if not fichas:
        print("\nNenhuma ficha cadastrada para excluir!")
        input("Pressione Enter para voltar...")
        return

    while True:
        print("\n" + "=" * 40)
        print("EXCLUIR FICHA".center(40))
        print("=" * 40)

        for i, ficha in enumerate(fichas, 1):
            print(f"{i}. {ficha['nome']} ({ficha['categoria']})")

        try:
            escolha = int(input("\nDigite o número da ficha que deseja excluir: "))
            if escolha < 1 or escolha > len(fichas):
                print("Opção inválida!")
                continue
        except ValueError:
            print("Entrada inválida!")
            continue

        ficha_encontrada = fichas[escolha - 1]

        print("\nFicha encontrada:")
        print(f"Nome: {ficha_encontrada['nome']}")
        print(f"Categoria: {ficha_encontrada['categoria']}")
        print("\nIngredientes:")
        for i in ficha_encontrada['ingredientes']:
            print(f"- {i['quantidade']} de {i['ingrediente']}")
        print("\nModo de Preparo:")
        for p in ficha_encontrada['preparo']:
            print(f"{p['passo']}. {p['descricao']}")
        print("-" * 40)

        confirmar = input(f"Tem certeza que deseja excluir a ficha '{ficha_encontrada['nome']}'? (s/n): ").lower()
        if confirmar == 's':
            fichas.remove(ficha_encontrada)
            salvar_fichas(fichas)
            print("Ficha excluída com sucesso!")
        else:
            print("Exclusão cancelada.")

        if input("\nDeseja excluir outra ficha? (s/n): ").lower() != 's':
            break

def menu_fichas():
    while True:
        fichas = carregar_fichas()
        
        print("\n--- MENU FICHAS ---")
        print("1. Adicionar Ficha")
        print("2. Visualizar Fichas")
        print("3. Editar Ficha")
        print("4. Excluir Ficha")
        print("0. Voltar")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            adicionar_ficha(fichas)
        elif opcao == "2":
            visualizar_fichas(fichas)
        elif opcao == "3":
            editar_fichas(fichas)
        elif opcao == "4":
            excluir_fichas(fichas)
        elif opcao == "0":
            return
        else:
            print("\nOpção inválida!")

if __name__ == "__main__":
    menu_fichas()