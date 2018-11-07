sshpass -p $1 ssh -o StrictHostKeyChecking=no root@$2 <<-'ENDSSH'
    cd 2018.2-NaturalSearch/
    docker-compose -f docker-compose.deploy.yml down
    docker rmi $(docker images -q) -f 
    docker-compose -f docker-compose.deploy.yml up -d
    docker-compose run web bash
    python manage.py makemigrations
    python manage.py migrate
ENDSSH