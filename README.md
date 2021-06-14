This is a test project for a junior Python Developer position

1. Clone the project to your server/machine
2. Type commands:
    docker-compose build
    docker-compse up -d
3. After starting the containers create migrations  
    docker-compose exec web ./manage.py makemigrations                      
   docker-compose exec web ./manage.py migrate
4. Create a superuser using this command            
docker-compose exec web ./manage.py createsuperuser
            
In case of errors use Google or StackOverFlow

Working API's are here: http://194.58.92.212:8020

