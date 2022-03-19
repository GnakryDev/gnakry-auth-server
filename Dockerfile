FROM python:3.9.0-slim

WORKDIR /app

RUN pip install  poetry

COPY . /app

RUN poetry install

VOLUME [ "/app/config" ]

EXPOSE  80

ENTRYPOINT ["poetry", "run", "uvicorn",  "--host", "0.0.0.0", "--port", "80",  "gnakry_auth_server.main:app" ]
