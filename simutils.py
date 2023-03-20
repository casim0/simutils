import sys
import os
import time
from datetime import datetime
from pytz import timezone
from pathlib import Path
import shutil

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

def today_datetime():
    return datetime.now(timezone('Asia/Seoul')).strftime("%Y%m%dT%H%M%S")

def pathlib_path(path):
    if isinstance(path, Path):
        path = Path(path)
    return path

def shutil_copy(input_file, output_dir, file_name=None, ver=1):
    input_file = pathlib_path(input_file)
    output_dir = pathlib_path(output_dir)

    if not file_name:
        file_name = input_file.name

    if ver==2:
        shutil.copy2(input_file, output_dir / file_name)
    else :
        shutil.copy(input_file, output_dir / file_name)

# os 상관없이 경로 문제 해결을 위한 함수 및 객체 만들 예정 (아직 수정중)
# pathlib을 벤치마킹
# replace 활용
def os_path(p):
    nt_sep = p.split('\\')
    ot_sep = p.split('/')
    if nt_sep > ot_sep:
        sep = '\\'
    elif nt_sep < ot_sep:
        sep = '/'
    else :
        return p
    
    if os.name == 'nt':
        if sep == '\\':
            return p
        else :
            return '\\'.join(ot_sep)
    else :
        if sep == '/':
            return p
        else :
            return '/'.join(nt_sep)