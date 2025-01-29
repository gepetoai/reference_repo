import time
from src.db.supabase import SupabaseClient
from src.core.logging import get_logger
from src.worker.tasks import  celery_app

db = SupabaseClient()
logger = get_logger('celery')



if __name__ == "__main__":
    try:  
        celery_app.start(argv=['worker','--concurrency=1' , '--loglevel=info'])
        while True:
            time.sleep(1)
            pass
    except Exception as e:
        logger.exception('Exception in celery %s ::', e)