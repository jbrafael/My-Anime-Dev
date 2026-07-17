# My Anime Dev 🎌

É uma aplicação web para gerenciamento de animes pessoais. Desenvolvido em **Django**, utilizando a **Kitsu API** para buscas em tempo real e **Tailwind CSS** para estilização da interface.

## Funcionalidades
- **Live Search**: Busca de animes em tempo real consumindo API externa sem recarregar a página.
- **CRUD Completo**: Adicionar, listar, editar status/notas e remover animes da lista pessoal.
- **Feedback Visual**: Toasts interativos de sucesso, informação e erro.
- **Persistência de Dados**: Utilização do SQLite para um armazenamento leve e eficiente.

## Tecnologias que utilizei
- Python 3 & Django
- Vanilla Javascript (Fetch API)
- Tailwind CSS (via CDN)
- SQLite

## Como rodar localmente

1. Clone este repositório.
2. Crie e ative o ambiente virtual:

   python -m venv venv
   source venv/bin/activate

   Instale as dependências:

pip install -r requirements.txt
Execute as migrações do banco de dados:


python manage.py migrate
Inicie o servidor de desenvolvimento:


python manage.py runserver
Acesse http://127.0.0.1:8000/ no seu navegador.

Desenvolvido por Jobson Rafael para a disciplina de Desenvolvimento web II
