# Super Analyst

**Super Analyst** é uma aplicação avançada de conversão de texto para SQL, utilizando a poderosa combinação do framework Vanna.ai, o modelo de linguagem GPT-4 da OpenAI e o armazenamento vetorial ChromaDB. O projeto foi desenvolvido para permitir a geração de consultas SQL complexas a partir de perguntas em linguagem natural, proporcionando uma maneira intuitiva e eficiente de interagir com bancos de dados.

## Índice

- [Visão Geral](#visão-geral)
- [Arquitetura](#arquitetura)
- [Como Começar](#como-começar)
- [Arquitetura e Decisões de Projeto](#arquitetura-e-decisões-de-projeto)
- [Contribuição](#contribuição)
- [Licença](#licença)
- [Contato](#contato)

## Visão Geral

**Super Analyst** transforma consultas em linguagem natural em SQL de forma eficiente e precisa, utilizando:

- **Vanna.ai**: Framework para desenvolvimento de aplicativos de NLP (Processamento de Linguagem Natural).
- **GPT-4 da OpenAI**: LLM (Modelo de Linguagem de Grande Escala) para entender e gerar consultas SQL.
- **ChromaDB**: Armazenamento vetorial para gerenciar e recuperar embeddings de consulta.
- **Python**: Linguagem de programação utilizada para a aplicação.
- **Webapp da Vanna.ai**: Interface web para interação com o sistema.

O modelo foi treinado com uma vasta quantidade de consultas SQL e perguntas para aprimorar sua capacidade de entender e gerar SQL a partir de perguntas complexas.

## Arquitetura

O projeto é composto pelos seguintes componentes principais:

1. **Frontend**: Desenvolvido com o webapp da Vanna.ai, proporciona uma interface amigável para os usuários interagirem com o sistema.
2. **Backend**:
   - **API**: Responsável por receber perguntas e retornar consultas SQL geradas.
   - **Vanna.ai Framework**: Facilita a comunicação entre a interface e o modelo LLM.
   - **GPT-4**: Modelo de linguagem que interpreta as perguntas e gera a consulta SQL correspondente.
   - **ChromaDB**: Utilizado para armazenar e recuperar vetores de embeddings para consultas rápidas e precisas.

## Como Começar

### Pré-requisitos

- Python 3.12.4
- Dependências listadas no arquivo `requirements.txt`
- Chave de API para GPT-4 da OpenAI
- Conta e configuração do Vanna.ai
- Configuração do ChromaDB

### Instalação

Clone o repositório:

```bash
git clone https://github.com/seuusuario/super-analyst.git
cd super-analyst
```

Na pasta enviroments da raiz, crie 3 arquivos ".env" para as configurações da aplicação com as seguintes variáveis abaixo:

- api-config.env
```bash
API_KEY="your-openAI-apiKey"
```

- db-config.env
```bash
DB_HOST="your-MySQL-Database"
DB_NAME="your-database-name"
DB_USER="your-database-user"
DB_PASS="your-database-password"
DB_PORT=your-database-port
```

- user-config.env
```bash
EMAIL="seuemail@seudominio.com"
PASSWORD="SuaSenha"
```
Instale as dependências:

```bash
pip install -r requirements.txt
```

### Execução

Para iniciar o aplicativo, utilize o comando:

```bash
python main.py
```

Se preferir rodar através de um docker, basta entrar na pasta raiz do repositório e utilizar o comando:

```bash
docker run -d -p 8084:8084 --name super-analyst superanalyst
```

Acesse o webapp através do navegador na URL http://localhost:8084, faça login com o usuário e senha de teste que você configurou em user-config.env e teste a aplicação.

## Arquitetura e Decisões de Projeto

### Arquitetura Geral

1. **Frontend**: Utilizado o WebApp da Vanna.ai que oferece uma experiência de usuário fluida e intuitiva.
2. **Backend**:
   - **Vanna.ai Framework**: Facilita o processamento de NLP e a interação com o modelo GPT-4.
   - **GPT-4**: Treinado para gerar SQL a partir de linguagem natural.
   - **ChromaDB**: Fornece armazenamento e recuperação eficiente de embeddings.

#### Architectural Decision Record (ADR)

**ADR 001: Escolha do Modelo de Linguagem**
- **Decisão**: Utilizar GPT-4 da OpenAI.
- **Justificativa**: GPT-4 oferece capacidade superior de compreensão e geração de texto em comparação com versões anteriores e outros modelos disponíveis.

**ADR 002: Armazenamento Vetorial**
- **Decisão**: Adotar ChromaDB.
- **Justificativa**: ChromaDB foi escolhido por sua performance em operações de armazenamento e recuperação de embeddings.

**ADR 003: Framework de NLP**
- **Decisão**: Optar pelo Vanna.ai.
- **Justificativa**: O Vanna.ai fornece um framework robusto para a integração de modelos de linguagem e desenvolvimento de aplicativos NLP.

## Contribuição

Contribuições são bem-vindas! Para colaborar com o projeto, siga estes passos:

1. Faça um fork do repositório.
2. Crie uma branch para sua feature (`git checkout -b feature/novafeature`).
3. Faça commit das suas alterações (`git commit -am 'Adiciona nova feature'`).
4. Envie para o repositório (`git push origin feature/novafeature`).
5. Crie um Pull Request.

## Contato

Para dúvidas ou sugestões, entre em contato através de [rpdesenvolvimento92@gmail.com](mailto:rpdesenvolvimento92@gmail.com).

---

Sinta-se à vontade para ajustar ou expandir as seções conforme necessário para se adequar às suas necessidades específicas!