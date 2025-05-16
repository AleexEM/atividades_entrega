# 🔍 Buscador de Notícias com NewsAPI

Este é um script em Python que permite ao usuário buscar notícias em tempo real sobre qualquer tema, utilizando a [NewsAPI](https://newsapi.org/).  
O usuário escolhe o tema e a quantidade de notícias (máximo de 5), e o programa retorna as informações principais de cada notícia.

---

## 📌 Funcionalidades

- Menu interativo no terminal
- Busca de notícias por palavra-chave
- Limite de até 5 notícias por pesquisa
- Mostra:
  - Título
  - Descrição
  - Autor
  - Link da notícia
- Histórico dos temas pesquisados

---

## ⚙️ Tecnologias Utilizadas

- Python 3
- [requests](https://pypi.org/project/requests/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

---

## 📦 Instalação

1. Clone o repositório:

```bash
git clone https://github.com/AleexEM/atividades_entrega
cd atividades_entrega
```

## 🧠 Uso do GPT

1. Criação da documentação em docstring das funções  
2. Definição e aplicação do limite de quantas pesquisas o usuário pode fazer  
3. Auxílio na criação e estruturação do README  


# 🌐 Visualizador de Posts com API Fake (ATIVIDADE 2)

Este projeto é um sistema simples de terminal que simula um pequeno cliente de rede social. Ele permite visualizar posts e comentários, criar novos posts, e visualizar posts de usuários específicos utilizando a API pública [JSONPlaceholder](https://jsonplaceholder.typicode.com/).

## ✅ Funcionalidades

- Login simulado com usuário fixo
- Menu interativo com as opções:
  - Visualizar os 5 primeiros posts e seus comentários
  - Criar um novo post
  - Ver posts do usuário logado
  - Ver posts de outro usuário (ID de 1 a 10)
- Exibição de um resumo final com:
  - Total de posts visualizados
  - Total de comentários visualizados
  - Total de posts criados

## 🔧 Tecnologias utilizadas

- Python 3
- Biblioteca `requests` para chamadas HTTP
- Biblioteca `dotenv` para variáveis de ambiente (login/senha)

## ▶️ Como rodar

1. Clone o repositório ou copie os arquivos para sua máquina.
2. Instale as dependências (se ainda não tiver):
   ```bash
   pip install requests python-dotenv

 