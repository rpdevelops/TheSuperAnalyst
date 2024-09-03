# Super Analyst

**Super Analyst** Is an advanced text-to-SQL application using the powerful combination of the Vanna.ai framework, OpenAI's GPT-4 language model, and ChromaDB vector storage. The project was developed to allow the generation of complex SQL queries from natural language questions, providing an intuitive and efficient way to interact with databases.

## Índice

- [Overview](#Overview)
- [Architecture](#Architecture)
- [Get Started](#gettind-started)
- [Architectural Decision Records](#architectural-decision-records)
- [Contribution](#contribution)
- [Licence](#licence)
- [Contact](#contact)

## Overview

**Super Analyst** transforms natural language queries into SQL efficiently and accurately, using:

- **Vanna.ai**: Framework for developing NLP (Natural Language Processing) applications.
- **GPT-4 da OpenAI**: LLM (Large Scale Language Model) to understand and generate SQL queries.
- **ChromaDB**: Vector storage to manage and retrieve query embeddings.
- **Python**: Programming language used for the application.
- **Webapp da Vanna.ai**: Web interface for interacting with the system.

The model has been trained with a vast amount of SQL queries and questions to enhance its ability to understand and generate SQL from complex questions.

## Architecture

The project is composed of the following main components:

1. **Frontend**: Developed with the Vanna.ai webapp, it provides a friendly interface for users to interact with the system.
2. **Backend**:
   - **API**: Responsible for receiving questions and returning generated SQL queries.
   - **Vanna.ai Framework**: Facilitates communication between the interface and the LLM model.
   - **GPT-4**: Language model that interprets questions and generates the corresponding SQL query.
   - **ChromaDB**: Used to store and retrieve embedding vectors for fast and accurate queries.

## Gettind Started

### Prerequisites

- Python 3.12.4
- Dependencies listed in the file `requirements.txt`
- OpenAI GPT-4 API Key
- ChromaDB Configuration

### Instalation

Clone the repository:

```bash
git clone https://github.com/seuusuario/super-analyst.git
cd super-analyst
```

In the root environments folder, create 3 ".env" files for the application settings with the following variables below:

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
EMAIL="yourEmail@YourDomain.com"
PASSWORD="YourPassword"
```
Install the dependencies:

```bash
pip install -r requirements.txt
```

### Running:

To start the application, use the command:

```bash
python main.py
```

If you prefer to run through Docker, just enter the repository root folder and run the command:

```bash
docker run -d -p 8084:8084 --name super-analyst superanalyst
```

Access the webapp through the browser at the URL http://localhost:8084, log in with the test username and password that you configured in user-config.env and test the application.

## Architectural Decision Records

### Architectural Decision Record (ADR)

**ADR 001: Choice of Language Model**
- **Decision**: Use GPT-4 from OpenAI.
- **Justification**: GPT-4 offers superior text comprehension and generation capabilities compared to previous versions and other available models.

**ADR 002: Vector Storage**
- **Decision**: Adopt ChromaDB.
- **Justification**: ChromaDB was chosen for its performance in embedding storage and retrieval operations.

**ADR 003: NLP Framework**
- **Decision**: Choose Vanna.ai.
- **Justification**: Vanna.ai provides a robust framework for integrating language models and developing NLP applications.

## Contribution

Contributions are welcome! To collaborate with the project, follow these steps:

1. Fork the repository.
2. Create a branch for your feature (`git checkout -b feature/novafeature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the repository (`git push origin feature/novafeature`).
5. Create a Pull Request.

## Contact

For questions or suggestions, please contact [rpdesenvolvimento92@gmail.com](mailto:rpdesenvolvimento92@gmail.com).

---

Feel free to adjust or expand the sections as needed to fit your specific needs!
