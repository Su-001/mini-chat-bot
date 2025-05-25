# mini_chat_bot with PostgreSQL & Docker

This is a simple conversational chatbot powered by [Mistral](https://docs.mistral.ai/) that stores user interactions in a PostgreSQL database. The entire app is containerized using Docker and Docker Compose.

---

## 📁 Project Structure

```
mini_chat_bot/
├── mistral_chatbot.py      # Main chatbot script
├── database.py             # Handles DB connection and inserts
├── requirements.txt        # Python packages
├── Dockerfile              # Builds chatbot container
└── Pipfile / Pipfile.lock  # Optional (if using pipenv)
```

---

## 🚀 Features

- Uses [Mistral AI](https://mistral.ai/) for chat responses
- Stores all messages in a PostgreSQL database
- Fully Dockerized with `docker-compose`

---

## ⚙️ Prerequisites

- [Docker](https://www.docker.com/)
- A [Mistral API key](https://docs.mistral.ai/)

---

## 📦 Setup Instructions

### 1. Clone the project

```bash
git clone https://github.com/your-username/mini_chat_bot.git
cd mini_chat_bot
```

### 2. Create `.env` file

Create a `.env` file in the root folder:

```env
MISTRAL_API_KEY=your_mistral_api_key
POSTGRES_USER=postgres
POSTGRES_PASSWORD=yourpassword
POSTGRES_DB=dbname
POSTGRES_HOST=localhost
POSTGRES_PORT=5432

```

---

### 3. Build and run with Docker

```bash
docker build -t mistral-chatbot .


docker run --rm -it \
  -e MISTRAL_API_KEY=api_key \
  -e POSTGRES_HOST=host.docker.internal \
  -e POSTGRES_USER=dbusername \
  -e POSTGRES_PASSWORD=password \
  -e POSTGRES_DB=dbname \
  -e POSTGRES_PORT=dbport \
  mistral-chatbot
```

This will:
- Start PostgreSQL database container
- Build the chatbot container
- Run your chatbot in an interactive terminal

---

## 💬 How It Works

1. User enters their name and a message.
2. The chatbot responds using Mistral.
3. The chat (user + bot message) is saved to PostgreSQL.

---

## 🗃️ Database Table

Table: `chat_logs`

| Column        | Type      |
|---------------|-----------|
| id            | SERIAL PRIMARY KEY |
| username      | TEXT      |
| user_message  | TEXT      |
| bot_response  | TEXT      |
| timestamp     | TIMESTAMP (default now) |

---

## 🧪 Running Locally Without Docker (Optional)

If you'd like to run it without Docker:

```bash
pipenv install
pipenv shell
pip install -r requirements.txt

export MISTRAL_API_KEY=your_mistral_api_key
export POSTGRES_USER=postgres
export POSTGRES_PASSWORD=yourpassword
export POSTGRES_DB=dbname
export POSTGRES_HOST=localhost
export POSTGRES_PORT=5432

python mistral_chatbot.py
```
---

## 📝 License

MIT – Use this for learning and personal projects!

---

## 🙋‍♀️ Author

Made with ❤️ by Suhani
