FROM python:3.10-slim

WORKDIR /usr/src/app

COPY . .

RUN pip install websockets aiohttp

EXPOSE 65432 8081

CMD ["python", "main.py"]
