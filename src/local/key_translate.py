"""
Controller that translates keystrokes into function calls
"""
from evdev_handler import scan_key_events_loop, select_event_device


class KeyTranslator:
    """KeyTranslator"""

    def __init__(self):
        """__init__"""

        self.up_keys = ["KEY_UP", "KEY_W"]
        self.down_keys = ["KEY_DOWN", "KEY_S"]
        self.forward_keys = []
        self.backward_keys = []
        self.left_keys = ["KEY_LEFT", "KEY_A"]
        self.right_keys = ["KEY_RIGHT", "KEY_D"]

        self.authorized_keys = []
        for keys in [
            self.up_keys,
            self.down_keys,
            self.forward_keys,
            self.backward_keys,
            self.left_keys,
            self.right_keys,
        ]:
            self.authorized_keys.extend(keys)

    def move_up(self):
        """Move Up"""

    def move_down(self):
        """Move Down"""

    def move_forward(self):
        """Move Forward"""

    def move_backward(self):
        """Move Backward"""

    def move_left(self):
        """Move Left"""

    def move_right(self):
        """Move Right"""

    @scan_key_events_loop()
    def key_to_move(self, event):
        """Translate keys and their state into functions

        Args:
            - events (dict): A dictionary containing the code and state as follows:
                ```
                {
                    "keycode": (str) keycode,       # Key code e.g. "KEY_ENTER"
                    "raw_code": (int) raw_code,     # Key code e.g. 28
                    "keystate": (str) keystate,     # Key state e.g. "down"
                    "raw_state": (int) raw_state,   # Key state e.g. 1
                }
                ```
        """

        if event["keycode"] not in self.authorized_keys:
            return

        if event["keystate"] == "up":
            print(f"Stop")
        else:
            if event["keycode"] in self.up_keys:
                print(f"Presionaste {event['keycode']}")
            if event["keycode"] in self.down_keys:
                print(f"Presionaste {event['keycode']}")
            if event["keycode"] in self.left_keys:
                print(f"Presionaste {event['keycode']}")
            if event["keycode"] in self.right_keys:
                print(f"Presionaste {event['keycode']}")

    def start(self):
        """start"""

        self.key_to_move()


if __name__ == "__main__":
    pass
