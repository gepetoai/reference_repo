from celery import Celery
from app.core.config import settings
from app.monitoring.logging import get_logger

logger = get_logger(__name__)

class CeleryClient:
    def __init__(self):
        self.celery_app = Celery('tasks', broker=settings.CELERY_BROKER_URL)

    def create_task(self, task_name: str):
        def task_decorator(func):
            try:
                self.celery_app.task(name=task_name)(func)
                return func
            except Exception as e:
                logger.error(f"Failed to create task {task_name}: {str(e)}")
                raise RuntimeError(f"Failed to create task {task_name}: {str(e)}")
        return task_decorator

    def run_task(self, task_name: str, *args, **kwargs):
        try:
            return self.celery_app.send_task(task_name, args=args, kwargs=kwargs)
        except Exception as e:
            logger.error(f"Failed to run task {task_name}: {str(e)}")
            raise RuntimeError(f"Failed to run task {task_name}: {str(e)}")




# Example Usage

from app.clients.worker.celery_client import CeleryClient


celery_client = CeleryClient()

# Step 2: Define a task
@celery_client.create_task('my_task')
def my_task(x, y):
    try:
        return x + y
    except Exception as e:
        logger.error(f"Failed to execute task my_task: {str(e)}")
        raise RuntimeError(f"Failed to execute task my_task: {str(e)}")

# Step 3: Run the task
result = celery_client.run_task('my_task', 5, 10)
logger.info(f"Task result: {result}")