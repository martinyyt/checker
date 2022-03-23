#!/usr/bin/env python3

from logger import logger
from datetime import datetime
import time
import requests
import sys
from elapsed_time_decorator import elapsed_time

class Checker:
  def __init__(self, run=10, sleep=1, **kwargs):
      self._sleep = int(sleep)
      self._run = float(run)
      if 'url' in kwargs:
        self._url = kwargs['url']
      else:
        raise TypeError(f'url parameter is required')
      
  def __str__(self) -> str:
      return f'sleep: {self._sleep}s, run: {self._run}m, url: {self._url}'
    
  def check(self):
    last_msg = ''
    stop = int(self._run * 60 + 1)
    for i in range(0, stop, self._sleep):
      try:
        response = requests.get(url=self._url)
        msg = response.status_code
      except Exception as e:
        msg = e
        
      if not (msg == last_msg and i < stop - 1):
        logger.info(f'UTC: {datetime.utcnow().isoformat()} -> Status code: {msg}')
        
      last_msg = msg
      time.sleep(self._sleep)
     
@elapsed_time
def main():
  checker = Checker(**dict(arg.split('=') for arg in sys.argv[1:]))
  logger.info(f'\nchecker: {checker}')
    
  checker.check()
  print(f'END, logs output file logs.log created.')
      
if __name__ == "__main__":
  main()
