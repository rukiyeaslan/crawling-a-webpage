FROM python:3.8

WORKDIR /app

COPY main.py requirements.txt /app/

RUN pip install uvicorn -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
