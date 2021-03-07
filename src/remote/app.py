"""
Start Remote side
"""
from flask import Flask

import pan_tilt
from pan_tilt import pan_servo, tilt_servo

# ----------------------------------------------------------------------------------------------- #
# General Config
# ----------------------------------------------------------------------------------------------- #
app = Flask(__name__)

# Servo config
servos = [pan_servo, tilt_servo]
pan_tilt.set_angle(servos, 90)
tilt_angle = 90
pan_angle = 90


# ----------------------------------------------------------------------------------------------- #
# Main Program
# ----------------------------------------------------------------------------------------------- #
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

    global tilt_angle
    tilt_angle -= 5
    if tilt_angle < 0:
        tilt_angle = 0
    pan_tilt.set_angle(tilt_servo, tilt_angle)
    return f"Set angle to {tilt_angle} degrees.\n"

@app.route("/down")
def move_down():
    """Move Down"""

    global tilt_angle
    tilt_angle += 5
    if tilt_angle < 180:
        tilt_angle = 180
    pan_tilt.set_angle(tilt_servo, tilt_angle)
    return f"Set angle to {tilt_angle} degrees.\n"


if __name__ == "__main__":
    app.run()