FROM python:3.9.2

RUN mkdir /app
WORKDIR /app
ADD . /app/
RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python3", "/app/bancoEndpoint.py"]
