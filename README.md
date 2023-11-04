[![volunteer](https://github.com/IvanSerbeniuk/volunteer/actions/workflows/docker-build-push.yml/badge.svg)](https://github.com/IvanSerbeniuk/volunteer/actions/workflows/docker-build-push.yml)


loadtest -n 100 -k  http://localhost:8000/

loadtest -t 300 -c 4 --rps 20  http://localhost:8000/

sudo docker-compose -f docker-compose.yaml up --build -d

docker exec -it volunteer python manage.py migrate

git tag -a v0.2.5 -m "my version v0.2.5"

git push origin v0.2.4

scp  -o StrictHostKeyChecking=no -r init-letsencrypt.sh ubuntu@IP:/home/ubuntu/app