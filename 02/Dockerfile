FROM python:3.11-alpine

RUN pip3 --no-cache-dir install fastapi uvicorn

EXPOSE 8087

COPY ./app /app

CMD uvicorn app.main:app --host 0.0.0.0 --port 8087

# docker build -t <nome-imagem> .
# docker run -d -p 8087:8087 --rm --name <nome-imagem-execucao> <nome-imagem>
 
 
    