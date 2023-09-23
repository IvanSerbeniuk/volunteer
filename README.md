

loadtest -n 100 -k  http://localhost:8000/

loadtest -t 300 -c 4 --rps 20  http://localhost:8000/

sudo docker-compose -f docker-compose.yaml up --build -d

docker exec -it volunteer python manage.py migrate