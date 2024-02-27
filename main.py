from pywebio.input import input, NUMBER
from pywebio.output import put_text, use_scope,put_buttons
from pywebio.exceptions import SessionClosedException
from pywebio import *
import os

def start(test=''):
    stream = os.popen('python prog.py')
    output = stream.read()
    put_text(output)


def main():
    try:
        put_buttons(['start'],onclick=start)
    except SessionClosedException:
        print("The session was closed unexpectedly")

start_server(main, port=8880, debug=True)
