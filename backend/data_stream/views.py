from rest_framework.decorators import api_view
from rest_framework.response import Response
from .tasks import my_long_running_task

@api_view(['POST'])
def start_task(request):
    my_long_running_task.delay()
    
    return Response({"status": "Task started"})
