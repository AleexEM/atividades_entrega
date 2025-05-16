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

# Estas variáveis vão guardar os totais enquanto o programa roda
total_posts_vistos = 0
total_comentarios_vistos = 0
total_posts_criados = 0

  

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
    """)
    return input("Escolha uma opção: ")

# def visualiza_comentarios():

#     url = "https://jsonplaceholder.typicode.com/posts/1/comments"


#     resposta = requests.get(url=url)
#     resposta_json  = resposta.json()

#     for comentario in resposta_json:
#         print("\n")
#         print(f"Usuario: {comentario['email']}")
#         print(f"Descrição: {comentario['body']}")

def visualiza_posts_e_comentarios():
    global total_posts_vistos, total_comentarios_vistos

    url_posts = "https://jsonplaceholder.typicode.com/posts"

    resposta = requests.get(url_posts)

    if resposta.status_code != 200:
        print("Erro ao buscar posts.")
        return

    posts = resposta.json()

    # Pegamos os 5 primeiros posts da lista
    for post in posts[:5]:
        print("\n--- POST ---")
        print(f"ID: {post['id']}")
        print(f"Título: {post['title']}")
        print(f"Conteúdo: {post['body']}")
        total_posts_vistos += 1

        # Busca os comentários de cada post
        url_comentarios = f"https://jsonplaceholder.typicode.com/posts/{post['id']}/comments"
        resposta_coment = requests.get(url_comentarios)

        if resposta_coment.status_code == 200:
            comentarios = resposta_coment.json()
            print(f"\nComentários ({len(comentarios)}):")
            for comentario in comentarios:
                print(f"- {comentario['email']}: {comentario['body']}")
            total_comentarios_vistos += len(comentarios)
        else:
            print("Não foi possível carregar os comentários.")

def ver_meus_posts():
    global total_posts_vistos

    user_id = 1  # Simulação pro meu usuario

    url = f"https://jsonplaceholder.typicode.com/posts?userId={user_id}"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        meus_posts = resposta.json()
        print(f"\nVocê possui {len(meus_posts)} posts:")
        for post in meus_posts:
            print("\n--- MEU POST ---")
            print(f"Título: {post['title']}")
            print(f"Conteúdo: {post['body']}")
            total_posts_vistos += 1
    else:
        print("Erro ao buscar seus posts.")

def ver_posts_de_outro_usuario():
    global total_posts_vistos

    user_id = input("Digite o ID do usuário que deseja ver os posts (1 a 10): ")

    url = f"https://jsonplaceholder.typicode.com/posts?userId={user_id}"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        posts = resposta.json()
        if posts:
            print(f"\nO usuário {user_id} possui {len(posts)} posts:")
            for post in posts:
                print("\n--- POST DO USUÁRIO ---")
                print(f"Título: {post['title']}")
                print(f"Conteúdo: {post['body']}")
                total_posts_vistos += 1
        else:
            print("Este usuário não possui posts.")
    else:
        print("Erro ao buscar os posts.")

def criar_novo_post():
    global total_posts_criados

    user_id = 1  # Simulação do usuário alex.meurer

    titulo = input("Digite o título do post: ")
    corpo = input("Digite o conteúdo do post: ")

    url = "https://jsonplaceholder.typicode.com/posts"
    dados = {
        "userId": user_id,
        "title": titulo,
        "body": corpo
    }

    resposta = requests.post(url, json=dados)

    if resposta.status_code == 201:
        print("\nPost criado com sucesso!")
        print(f"ID do novo post: {resposta.json().get('id')}")
        total_posts_criados += 1
    else:
        print("Erro ao criar o post.")   

def mostrar_resumo():
    print("\n===== RESUMO DA SESSÃO =====")
    print(f"Posts visualizados: {total_posts_vistos}")
    print(f"Comentários visualizados: {total_comentarios_vistos}")
    print(f"Posts criados: {total_posts_criados}")
    print("=============================")


while True:
    login = input("Digite seu login: ")
    senha = input("Digite sua senha: ")

    if login == usuario['login'] and senha == usuario["password"]:
        print("Login realizado com sucesso!")
        break
    else:
        print("Usuário ou senha incorreto! Digite novamente.")

while True:
        
    opcao = menu()

    if opcao == "0":
        mostrar_resumo()
        print("Saindo do programa.")
        break
    elif opcao == "1":
        visualiza_posts_e_comentarios()
    elif opcao == "2":
        criar_novo_post()
    elif opcao == "3":
        ver_meus_posts()
    elif opcao == "4":
        ver_posts_de_outro_usuario()
    else:
        print("Opção inválida.")
