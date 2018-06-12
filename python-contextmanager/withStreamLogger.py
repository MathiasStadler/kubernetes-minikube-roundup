# from here
# https://stackoverflow.com/questions/41216145/context-manager-for-logging-equivalent-to-contextmanager-yield-stdout

import os
import logging
import subprocess

from io import IOBase
from sys import stdout
from select import select
from threading import Thread
from time import sleep

log = logging.getLogger(__name__)


class StreamLogger(IOBase):
    _run = None

    def __init__(self, logger_obj, level):
        super(StreamLogger, self).__init__()
        self.logger_obj = logger_obj
        self.level = level
        self.pipe = os.pipe()
        self.thread = Thread(target=self._flusher)
        self.thread.start()

    def __call__(self): return self

    def _flusher(self):
        self._run = True
        buf = b''
        while self._run:
            for fh in select([self.pipe[0]], [], [], 1)[0]:
                buf += os.read(fh, 1024)
                while b'\n' in buf:
                    data, buf = buf.split(b'\n', 1)
                    self.write(data.decode())
            sleep(1)
        self._run = None

    def write(self, data): return self.logger_obj.log(self.level, data)

    def fileno(self): return self.pipe[1]

    def close(self):
        if self._run:
            self._run = False
            while self._run is not None:
                sleep(1)
            os.close(self.pipe[0])
            os.close(self.pipe[1])


with StreamLogger(log, logging.INFO) as out, StreamLogger(log,
                                                          logging.ERROR) as err:
    subprocess.Popen('ls 1>&2', stderr=err, shell=True)
