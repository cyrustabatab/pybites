from itertools import cycle
import sys
from time import time, sleep

SPINNER_STATES = ['-', '\\', '|', '/']  # had to escape \
STATE_TRANSITION_TIME = 0.1


def spinner(seconds):
    """Make a terminal loader/spinner animation using the imports above.
       Takes seconds argument = time for the spinner to run.
       Does not return anything, only prints to stdout."""
    
    cycles = cycle(SPINNER_STATES)

    while True:
        s = next(cycles)
        print(s,end='\r')
        
        sleep(STATE_TRANSITION_TIME)


if __name__ == '__main__':
    spinner(2)
