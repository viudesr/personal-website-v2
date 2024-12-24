FROM python:3.11

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip

COPY src/requirements.txt .

RUN pip install -r requirements.txt

COPY src .

ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]

EXPOSE 8000