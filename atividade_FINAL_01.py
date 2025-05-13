import os
import requests
from dotenv import load_dotenv

load_dotenv()

def menu():
    """
    Mostra um menu de opções para o usuário e retorna a escolha feita.
    """

    print("\nMenu de opções:")
    print("""
    0 - Sair
    1 - Pesquisar uma noticia
    """)
    return input("Escolha uma opção: ")

def news(parametro1, parametro2):

    """
    Busca notícias relacionadas a uma palavra-chave e exibe uma quantidade limitada de resultados.

    Parâmetros:
    parametro1 (str): Palavra-chave para pesquisar nas notícias.
    parametro2 (int): Quantidade de notícias que serão exibidas.

    A função usa a API do NewsAPI e mostra para cada notícia:
    - Título
    - Descrição
    - Link para a matéria completa
    - Autor
    """
    while parametro2 > 5:
        print("="*20)
        print("Você só pode buscar no máximo 5 notícias por vez.")
        print("="*20)
        return

    api_key = os.getenv("API_KEY_NEWS")
    
    url = "https://newsapi.org/v2/everything"

    headers = {
        'x-api-key': api_key
    }

    params = {
        'q': parametro1,
        'language': "pt",
        'page': 1
        
    }

    resposta = requests.get(url=url, headers=headers, params=params)
    resposta_json  = resposta.json()


    for artigo in resposta_json["articles"][:parametro2]:
        print("\n")
        print(f"Titulo: {artigo['title']}")
        print(f"Descrição: {artigo['description']}")
        print(f"Acesse a materia completa: {artigo['url']}")
        print(f"Escrito por: {artigo['author']}")


temas_buscados = []
while True:
    opcao = menu()
    
    if opcao == "0":
        print(f'Você Pesquisou os Seguintes temas hoje:\n{temas_buscados}')
        print("Saindo do programa.")
        break

    elif opcao == "1":
        noticia = input("Quer Ver uma noticia sobre qual tema?")
        temas_buscados.append(noticia)
        quantas = int(input("E quer Ver quantas noticias sobre esse tema?"))
        news(noticia, quantas)

    else:
        print(f'Você Pesquisou os Seguintes temas hoje:\n{temas_buscados}')
        print("Opção inválida.")