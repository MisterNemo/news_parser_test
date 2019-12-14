**run project:**

`docker-compose build`

`docker-compose up -d`

`docker-compose run app python manage.py makemigrations`

`docker-compose run app python manage.py migrate`


**Test:**

`docker-compose run app pytest`


**parser request on demand**
`docker-compose run app python manage.py manual_request`
