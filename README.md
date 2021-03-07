## Interface for translating keystrokes into API calls

Basically, this project triggers an API call based on a pressed key. In the other side, the API will execute a function based on the call received. \
In particular, I use this project to control a couple of servos inside a pan-til support using [this](https://github.com/jfdona23/rpi-pan-tilt) library also made by me. I use a desktop computer as local and a raspberry pi as remote.

## Usage
_Note_: A python virtual environment is recommended.

### Local
When you run __start.py__ it will show you the event devices present in your computer. Please edit `EVENT_DEVICE` inside _src/local/evdev_handler.py_ with the correct event device number for you. Also you can set it using environmental variables.
```bash
pip install -r src/local/requirements.txt
# Root access in needed to get access to /dev/input/eventXX devices
sudo EVENT_DEVICE=15 REMOTE_URL=1.2.3.4 REMOTE_PORT=1234 python3 src/local/start.py
```

### Remote
You can set the IP:Port where the remote is going to listen by setting environmental variables or manually editing _src/remote/start.py_.
```bash
pip install -r src/remote/requirements.txt
LISTEN_HOST=1.2.3.4 LISTEN_PORT=1234 python3 src/remote/start.py
```