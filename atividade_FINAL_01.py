import os
import requests
from dotenv import load_dotenv

load_dotenv()

def menu():
    print("\nMenu de opções:")
    print("""
    0 - Sair
    1 - Pesquisar uma noticia
    """)
    return input("Escolha uma opção: ")

def news(parametro1, parametro2):
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
        print(artigo["title"])
        print(artigo["description"])
        print(artigo["url"])


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