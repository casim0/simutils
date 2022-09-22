import sys
import os
import time

class ProgBar(object):
    def __init__(self, total, decimals=2, bar_length=30, interval=0.05):
        self.total = total
        self.decimals = decimals
        self.bar_length = bar_length
        self.interval = interval
        
        self._num = 0
        self._last_update = 0
    
    def start(self):
        
        self._num += 1
        finalize = self._num >= self.total
        now = time.time()
        if now-self._last_update < self.interval and not finalize:
            return
        
        per = f'{(self._num/self.total)*100:.{self.decimals}f}'
        filled_length = int(round(self.bar_length * self._num / self.total))
        bar = '#' * filled_length + '-' * (self.bar_length - filled_length)
        sys.stdout.write(f'\r{self._num}/{self.total} |{bar}| {per}% ')
        if self._num == self.total: 
            sys.stdout.write('\n') 
        sys.stdout.flush() 
        
        self._last_update = now
        
class Timer(object):
    def __init__(self):
        self.s = 0
    
    def start(self):
        self.s = time.time()
        
    def end(self, digit=2, printer='Time'):
        e = time.time() - self.s 
        return print(f'{printer} : {round(e,digit)}s')

def separator():
    if os.name == 'nt':
        sep = '\\'
    else :
        sep = '/'
    return sep