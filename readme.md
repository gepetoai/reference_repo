#alembic commands 
docker compose run --rm web alembic revision --autogenerate -m "description" 

docker compose run --rm web alembic upgrade head

