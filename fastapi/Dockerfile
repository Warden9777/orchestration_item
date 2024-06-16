FROM python:latest
ENV MYSQL_HOST=mysql
ENV MYSQL_PORT=3306
ENV MYSQL_USER=root
ENV MYSQL_PASSWORD=maxmule
ENV MYSQL_DB=itemsDatabase
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY ./app /code/app
CMD ["fastapi", "run", "app/main.py", "--port", "80"]