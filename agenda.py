import json

def salvar_contatos(contatos):
    with open("contatos.txt", "w") as arquivo:
        json.dump(contatos, arquivo)

def carregar_contatos():
    try:
        with open("contatos.txt", "r") as arquivo:
            return json.load(arquivo)
    except:
        return {}

def adicionar_contato(contatos):
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    contatos[nome] = telefone
    salvar_contatos(contatos)
    print("Contato adicionado! ✅")

def ver_contatos(contatos):
    if len(contatos) == 0:
        print("Nenhum contato cadastrado!")
    else:
        for nome, telefone in contatos.items():
            print(nome, "→", telefone)

contatos = carregar_contatos()

while True:
    print("\n--- AGENDA ---")
    print("1 - Adicionar contato")
    print("2 - Ver contatos")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_contato(contatos)
    elif opcao == "2":
        ver_contatos(contatos)
    elif opcao == "3":
        print("Até logo!")
        break
    else:
        print("Opção inválida!")