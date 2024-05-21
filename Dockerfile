FROM python: 3.12.3

WORKDIR /app

COPY ./main.py /app
COPY ./requirements.txt /app

RUN pip3 install --no-cache-dir --upgrade -r /app/requirements.txt
CMD ["python3", "main.py"]

