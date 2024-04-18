FROM python:3.10

WORKDIR /app

COPY requirements.txt . 
RUN pip install -r requirements.txt

COPY . /app/
EXPOSE 8000

RUN python manage.py collectstatic --noinput
RUN python manage.py makemigration
RUN python manage.py migrate

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "restaurant.wsgi:applicaion"]