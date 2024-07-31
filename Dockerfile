FROM python:3.10

# Used For Disk Mounting
WORKDIR /home

COPY . .

# Most Of The Libraries That Are Used Are Built-In
RUN pip install rubpy
RUN pip install numexpr

CMD ["python3", "main.py"]