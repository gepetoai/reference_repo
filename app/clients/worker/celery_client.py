from celery import Celery

from app.config.app_config import settings
class CeleryClient:
    def __init__(self):
        self.celery_app = Celery('tasks', broker=settings.CELERY_BROKER_URL)

    def create_task(self, task_name: str):
        def task_decorator(func):
            self.celery_app.task(name=task_name)(func)
            return func
        return task_decorator

    def run_task(self, task_name: str, *args, **kwargs):
        return self.celery_app.send_task(task_name, args=args, kwargs=kwargs)




# Example Usage

from app.clients.worker.celery_client import CeleryClient


celery_client = CeleryClient()

# Step 2: Define a task
@celery_client.create_task('my_task')
def my_task(x, y):
    return x + y

# Step 3: Run the task
result = celery_client.run_task('my_task', 5, 10)
print(result)  # This will print the result of the task