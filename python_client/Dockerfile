FROM python:3.10-slim

WORKDIR /usr/src/app

COPY . .

RUN pip install websockets

# Run main.py when the container launches
CMD ["python", "main.py"]
