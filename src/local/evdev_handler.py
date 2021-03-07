"""
Lib for easily implement the evdev library
"""
import functools
import os

from evdev import InputDevice, categorize, ecodes

# ----------------------------------------------------------------------------------------------- #
# Constants
# ----------------------------------------------------------------------------------------------- #
EVENT_DEVICE = int(os.environ.get("EVENT_DEVICE", 0))


# ----------------------------------------------------------------------------------------------- #
# Main Program
# ----------------------------------------------------------------------------------------------- #
def get_event_devices():
    """get_event_devices"""

    devices = str()
    try:
        for i in range(100):
            devices += str(InputDevice("/dev/input/event" + str(i))) + "\n"
    except FileNotFoundError:
        pass

    return devices


def select_event_device(dev_number):
    """select_event_device"""

    dev = InputDevice("/dev/input/event" + str(dev_number))
    print(f"Selected device: {dev}")

    return dev


def get_device_capabilities(device, verbose=False):
    """get_device_capabilities"""

    return device.capabilities(verbose)


def scan_key_events_loop(device=select_event_device(EVENT_DEVICE)):
    """Decorator that returns parsed input events in loop

    Args:
        - device (InputDevice): evdev input device object

    Returns:
        - dict: A dictionary with the following structure:
            ```
            {
                "keycode":   "(str) Key code name",
                "raw_code":  "(int) Key code",
                "keystate":  "(str) Key state up/down/hold",
                "raw_state": "(int) Key state 0/1/2",
            }
            ```
    """

    def decorator_wrapper(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):

            try:
                os.system("stty -echo")  # Supress keystrokes echo during the loop
                keystate = ("up", "down", "hold")
                for event in device.read_loop():
                    if event.type == ecodes.EV_KEY:
                        evt = categorize(event)
                        parsed_event = {
                            "keycode": evt.keycode,
                            "raw_code": event.code,
                            "keystate": keystate[evt.keystate],
                            "raw_state": evt.keystate,
                        }
                        func(*args, parsed_event)
            except KeyboardInterrupt:
                print("Program aborted. Press CTRL + C to exit...")

        return wrapper

    return decorator_wrapper


if __name__ == "__main__":
    pass
