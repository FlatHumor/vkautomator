# coding=utf-8

import time


class LittleLooper(object):
    def __init__(self):
        self._callback = None
        self._callback_args = None
        self._period = 1
        self._stop_loop = False

    def set_callback(self, callback, **kwargs):
        self._callback = callback
        self._callback_args = kwargs

    def stop_loop(self):
        self._stop_loop = True

    def loop(self, func):
        while True and not self._stop_loop:
            value = func()
            if value:
                self._callback(value)
            time.sleep(self._period)