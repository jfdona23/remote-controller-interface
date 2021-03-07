"""
Start Local side
"""
from evdev_handler import get_event_devices
from key_translate import KeyTranslator


print(
    f"Showing Event devices: \n{get_event_devices()}\n"
    f">>> Edit the EVENT_DEVICE in evdev_handler.py constant according to your device\n"
)

key_translate = KeyTranslator()
key_translate.start()
