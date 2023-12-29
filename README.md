Instructions:

1. Clone repository
2. Create a .env file and add the following variables:
```
DATABASE_HOST=localhost
DATABASE_NAME=generator-tools
DATABASE_USER=postgres
#DATABASE_PASSWORD=
DATABASE_PORT=5432
APP_NAME="Email and Social Media Generator"
OPENAI_API_KEY={Your OpenAI API key}
```
   
3. Create the database and start the server with the following steps:
```
createdb generator-tools
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
alembic upgrade head
uvicorn main:app --reload
```

4. [Setup the front-end](https://github.com/szhu95/market-ai-app)
