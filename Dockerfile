FROM python:3.11

WORKDIR /usr/src/app

RUN pip install --upgrade pip

COPY src/requirements.txt .

RUN pip install -r requirements.txt

COPY src .

ENTRYPOINT ["python", "manage.py", "runserver"]