
# TODO NOT WORK
import sys
import os
from contextlib import *


def debug_trace(details):
    if __debug__:
        return TraceContext(details)
    # Don't do anything special with the context in release mode
    return ExitStack()


with debug_trace(stack):
    a = 1/0
