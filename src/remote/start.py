"""
Start Remote side
"""
import os

from flask import Flask

import pan_tilt
from pan_tilt import pan_servo, tilt_servo

# ----------------------------------------------------------------------------------------------- #
# General Config
# ----------------------------------------------------------------------------------------------- #
# Flask config
app = Flask(__name__)
LISTEN_HOST = os.environ.get("LISTEN_HOST", "0.0.0.0")
LISTEN_PORT = os.environ.get("LISTEN_PORT", "8080")

# Servo config
servos = [pan_servo, tilt_servo]
initial_angle = 90
pan_tilt.set_angle(servos, initial_angle)


# ----------------------------------------------------------------------------------------------- #
# Main Program
# ----------------------------------------------------------------------------------------------- #
@app.route("/reset")
def move_reset():
    """Movement Reset"""

    pan_tilt.set_angle(servos, initial_angle)
    return f"Set angle to {initial_angle} degrees.\n"


@app.route("/tilt/<int:angle>")
def move_tilt(angle):
    """Move tilt"""

    pan_tilt.set_angle(tilt_servo, angle)
    return f"Set Tilt to {angle} degrees.\n"


@app.route("/pan/<int:angle>")
def move_pan(angle):
    """Move pan"""

    pan_tilt.set_angle(pan_servo, angle)
    return f"Set Pan to {angle} degrees.\n"


@app.route("/up")
def move_up():
    """Move Up"""

    tilt_angle = pan_tilt.get_angle(tilt_servo) - 5
    if tilt_angle < 0:
        tilt_angle = 0
    pan_tilt.set_angle_smooth(tilt_servo, tilt_angle)
    return f"Set angle to {tilt_angle} degrees.\n"


@app.route("/down")
def move_down():
    """Move Down"""

    tilt_angle = pan_tilt.get_angle(tilt_servo) + 5
    if tilt_angle > 180:
        tilt_angle = 180
    pan_tilt.set_angle_smooth(tilt_servo, tilt_angle)
    return f"Set angle to {tilt_angle} degrees.\n"


@app.route("/left")
def move_left():
    """Move Left"""

    pan_angle = pan_tilt.get_angle(pan_servo) + 5
    if pan_angle > 180:
        pan_angle = 180
    pan_tilt.set_angle_smooth(pan_servo, pan_angle)
    return f"Set angle to {pan_angle} degrees.\n"


@app.route("/right")
def move_right():
    """Move Right"""

    pan_angle = pan_tilt.get_angle(pan_servo) - 5
    if pan_angle < 0:
        pan_angle = 0
    pan_tilt.set_angle_smooth(pan_servo, pan_angle)
    return f"Set angle to {pan_angle} degrees.\n"


# ----------------------------------------------------------------------------------------------- #
# Main Loop
# ----------------------------------------------------------------------------------------------- #
if __name__ == "__main__":
    app.run(host=LISTEN_HOST, port=LISTEN_PORT)