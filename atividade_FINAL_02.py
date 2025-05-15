import os
import requests
from dotenv import load_dotenv

load_dotenv()

# =========="BANCO DE DADOS"===========
usuario = {
    "login": "alex.meurer",
    "password": "senha123"
}
#=======================================

def menu():
    """
    Mostra um menu de opções para o usuário e retorna a escolha feita.
    """

    print("\nMenu de opções:")
    print("""
    0 - Sair
    1 - Visualizar POSTs e Comentarios:
    2 - Postar Algo:
    3 - Ver Meus Posts:
    4 - Ver Posts de outro usuario:
    5 - Ver Posts de outro usuario:
    """)
    return input("Escolha uma opção: ")

def visualiza_comentarios():

    url = "https://jsonplaceholder.typicode.com/posts/1/comments"


    resposta = requests.get(url=url)
    resposta_json  = resposta.json()

    for comentario in resposta_json:
        print("\n")
        print(f"Usuario: {comentario['email']}")
        print(f"Descrição: {comentario['body']}")


while True:

    login = input("Digite seu login")
    senha = input("Digite sua senha")

    if login == usuario['login'] and senha == usuario["password"]:

        opcao = menu()
    
        if opcao == "0":
            print("Saindo do programa.")
            break
        elif opcao == "1":
            visualiza_comentarios()
        elif opcao == "2":
            ...
        elif opcao == "3":
            ...
        elif opcao == "4":
            ...
        elif opcao == "5":
            ...
        else:
            print("Opção inválida.")

    else:
        print("Usuario ou senha incorreto! Digite Novamente.")
        continue
    