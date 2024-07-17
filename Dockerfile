FROM python:3.10

WORKDIR /home

COPY . .

RUN pip install rubpy
RUN pip install numexpr

CMD ["python3", "main.py"]