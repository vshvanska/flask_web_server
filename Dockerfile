FROM python:3.11-alpine

EXPOSE 5000

WORKDIR /src

COPY ./requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

RUN chmod +x entrypoint.sh

ENV FLASK_APP=app/app.py

ENTRYPOINT ["./entrypoint.sh"]
#ENTRYPOINT ["junicorn", "--bind", "0.0.0.0.:80", "app:create_app()"]
