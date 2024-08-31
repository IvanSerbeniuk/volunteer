[![volunteer](https://github.com/IvanSerbeniuk/volunteer/actions/workflows/docker-build-push.yml/badge.svg)](https://github.com/IvanSerbeniuk/volunteer/actions/workflows/docker-build-push.yml)

[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/IvanSerbeniuk/volunteer/blob/master/LICENSE.md)

loadtest -n 100 -k  http://localhost:8000/

loadtest -t 300 -c 4 --rps 20  http://localhost:8000/

sudo docker-compose -f docker-compose.yaml up --build -d

docker exec -it volunteer python manage.py migrate

git tag -a v0.2.5 -m "my version v0.2.5"

git push origin v0.2.4

scp  -o StrictHostKeyChecking=no -r init-letsencrypt.sh ubuntu@IP:/home/ubuntu/app

## License

See the [LICENSE](LICENSE.md) file for license rights and limitations (MIT).

python manage.py loaddata app/fixtures/authors.json

python manage.py dumpdata > db.json

python manage.py compilemessages --ignore=venv

python ../manage.py makemessages -l en

python manage.py runserver

venv\Scripts\Activate