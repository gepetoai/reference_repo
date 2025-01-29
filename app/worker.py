import time
from app.monitoring.logging import get_logger
from app.clients.worker.celery_client import CeleryClient

logger = get_logger('celery')

celery_app = CeleryClient()




if __name__ == "__main__":
    try:  
        celery_app.start(argv=['worker','--concurrency=1' , '--loglevel=info'])
        while True:
            time.sleep(1)
            pass
    except Exception as e:
        logger.exception('Exception in celery %s ::', e)
        raise e