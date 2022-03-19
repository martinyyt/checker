import time
from logger import logger

def elapsed_time(f):
  def wrapper():
    t1 = time.time()
    f()
    t2 = time.time()
    diff = t2 - t1
    seconds = diff % 60
    minutes = int(diff) // 60 % 60
    hours = int(diff) // 60 // 60
    logger.info(f'Elapsed time: {hours}h:{minutes}m:{round(seconds, 2)}s')
  return wrapper
