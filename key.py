from evdev import *
from time import time
from select import select


dev = InputDevice('/dev/input/event2')


def detect_key_hold(hold_time_sec=0.5):
    state = {}

    while True:
        # Block for a 100ms or until there are events to be read.
        r, _, _ = select([dev], [], [], 0.1)

        if r:
            for event in dev.read():
                if event.type == ecodes.EV_KEY:
                    # When the key is pressed, record its timestamp.
                    if event.value == 1:
                        state[event.code] = event.timestamp(), event
                    # When it's released, remove it from the state map.
                    if event.value == 0 and event.code in state:
                        del state[event.code]

        # Check if any keys have been held for longer than hold_time_sec seconds.
        now = time()
        for code, ts_event in list(state.items()):
            ts, event = ts_event
            if (now - ts) >= hold_time_sec:
                del state[code]  # only trigger once
                yield event
        continue


for event in detect_key_hold():
    print('%s is being held' % ecodes.KEY[event.code])