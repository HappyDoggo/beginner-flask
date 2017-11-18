from random import choice, randrange
from flask import Flask, render_template
"""
import flask and choice
"""

app = Flask(__name__)

def random_comp():
    return choice([
        "cute",
        "pretty",
        "cool",
        "valid",
        "worthy",
        "accepted",
        "welcomed"
        ])

def random_affirm():
    return choice([
        "okay",
        "alright",
        "real",
        "valid",
        "true"
        ])

def random_deserve():
    return choice([
        "better",
        "life",
        "happiness",
        "love",
        "acceptance"
        ])

def random_wish():
    return choice([
        "happy",
        "at peace",
        "true to yourself",
        "content"
        ])

def random_statement(number):
    switcher = {
        0: "You are {}.".format(random_comp()),
        1: "I'm telling you that it's {}.".format(random_affirm()),
        2: "You deserve {}.".format(random_deserve()),
        3: "I want you to be {}.".format(random_wish()),
    }

    return switcher.get(number, "It gets better.")

@app.route('/')
def hello_world():
    return render_template('gen.html', comp = random_comp(), affirm = random_statement(randrange(4)))
