FROM python:3.10.9

ENV PYTHONUNBUFFERED=1

# /build as the working directory
# RUN mkdir -p /app
WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python3", "manage.py", "runserver"]
