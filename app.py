import pywebio
from pywebio.platform.flask import webio_view
from flask import Flask, request, send_from_directory, current_app, url_for
from pywebio import STATIC_PATH
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *
import logging
from datetime import date, timedelta
from functools import partial
import time
from pywebio.session import info as session_info
import threading

app = Flask(__name__)


@app.route('/')
def hello():
    msg = f'<br/><a href="/tool">Start a new session</a>'
    return msg

def demo(test=''):
    
    put_text("Hello")
    age = input("What is your name? ")
    put_text(f"Hello {age}")
    #put_text("You are old")
    while age != 2:
        age = input("Enter your age: ", type=NUMBER)
        with use_scope('scope2', clear=True):  # enter the existing scope and clear the previous content
            put_text(f"you have selected {age}")
    put_text("you win")

def bmi():
    height = input("Input your height(cm)：", type=FLOAT)
    weight = input("Input your weight(kg)：", type=FLOAT)

    BMI = weight / (height / 100) ** 2

    top_status = [(16, 'Severely underweight'), (18.5, 'Underweight'),
                  (25, 'Normal'), (30, 'Overweight'),
                  (35, 'Moderately obese'), (float('inf'), 'Severely obese')]

    for top, status in top_status:
        if BMI <= top:
            put_text('Your BMI: %.1f. Category: %s' % (BMI, status))
            break


def start_flask_server():
    app.add_url_rule('/tool', 'webio_view', webio_view(demo), methods=['GET', 'POST', 'OPTIONS'])
    app.run(host='0.0.0.0', port=8888)


# if __name__ == '__main__':
#     t = threading.Thread(target=start_flask_server)
#     t.daemon = True
#     t.start()
#     webview.create_window('CEF Example', 'http://localhost:8888')
#     webview.start(gui='cef')

if __name__ == '__main__':
     start_flask_server()
#    app.add_url_rule('/tool', 'webio_view', webio_view(bmi), methods=['GET', 'POST', 'OPTIONS'])
#    webview.create_window('Flask example', app)
#    webview.start(gui='cef')