Для запуска контейнера
git clone https://github.com/AlexRich178/django-docker.git

docker build . -t docker-django

docker run -d -p 8000:8000 docker-django
