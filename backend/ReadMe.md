REDIS_HOST=os.environ.get('REDIS_HOST', "localhost")
REDIS_PORT=os.environ.get('REDIS_PORT', 6379)
# "host.docker.internal"   if the redis, celery in docker and django outside of the docker (local)
# "localhost" after docker-compose up (outside)

docker-compose up -d
uvicorn reacto_cast.asgi:application --host 0.0.0.0 --port 8000 --reload
