import os

from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "reacto_cast.settings")
app = Celery("data_stream")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


# # celery.py

# from __future__ import absolute_import, unicode_literals
# import os
# from celery import Celery

# # Set the default Django settings module for the 'celery' program.
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'reacto_cast.settings')

# # app = Celery('reacto_cast')
# app = Celery('reacto_cast', broker='redis://host.docker.internal:6379/0', backend='redis://host.docker.internal:6379/0')

# # Using Redis as the broker
# app.config_from_object('django.conf:settings', namespace='CELERY')

# # The URL to your Redis broker. 
# # Format: "redis://:password@hostname:port/db_number"
# # Default Redis runs on port 6379 and db_number is usually 0
# app.conf.broker_url = 'redis://host.docker.internal:6379/0'

# # If you're using a Redis instance managed by Docker and you're running Django locally:
# # app.conf.broker_url = 'redis://host.docker.internal:6379/0'

# # If you're using Redis in Docker for both Django and Redis:
# # app.conf.broker_url = 'redis://host.docker.internal:6379/0' # Where 'redis' is the service name in docker-compose.yml

# # Set the result backend (optional, only if you want to store task results)
# app.conf.result_backend = 'redis://host.docker.internal:6379/0'

# # Import task modules from all registered Django apps
# app.autodiscover_tasks()








# """# The URL to your Redis broker. 
# # Format: "redis://:password@hostname:port/db_number"
# # Default Redis runs on port 6379 and db_number is usually 0
# app.conf.broker_url = 'redis://localhost:6379/0'

# # If you're using a Redis instance managed by Docker and you're running Django locally:
# # app.conf.broker_url = 'redis://host.docker.internal:6379/0'

# # If you're using Redis in Docker for both Django and Redis:
# # app.conf.broker_url = 'redis://redis:6379/0' # Where 'redis' is the service name in docker-compose.yml

# # Set the result backend (optional, only if you want to store task results)
# app.conf.result_backend = 'redis://localhost:6379/0'"""