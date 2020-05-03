From python:3.7
ENV PYTHONBUFFERED 1

RUN mkdir /app
WORKDIR /app

EXPOSE 8000

COPY requirments.txt /app/
RUN pip install -r requirments.txt
COPY . /app/

CMD [ "python", "manage.py", "makemigrations", "--noinput"]
CMD [ "python", "manage.py", "migrate"]
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]