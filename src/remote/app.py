"""
Start Remote side
"""
from flask import Flask

import pan_tilt
from pan_tilt import pan_servo, tilt_servo

app = Flask(__name__)
servos = [pan_servo, tilt_servo]

@app.route("/up")
def move_up(self):
    """Move Up"""

    pan_tilt.set_angle(tilt_servo, 45)


@app.route("/down")
def move_down(self):
    """Move Down"""

    pan_tilt.set_angle(tilt_servo, 135)


@app.route("/forward")
def move_forward(self):
    """Move Forward"""


@app.route("/backward")
def move_backward(self):
    """Move Backward"""


@app.route("/left")
def move_left(self):
    """Move Left"""


@app.route("/right")
def move_right(self):
    """Move Right"""