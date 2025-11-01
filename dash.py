from pgl import *

# Constants
WINDOW = 400
TICK_MS = 100

# Derived Constants
BLOCK = WINDOW / 10
GROUND = WINDOW - BLOCK
GRAVITY = BLOCK / 4
FLOOR = GROUND - BLOCK # Blocks need to be placed block height above the ground to be on the floor.
DANGER = 3 * BLOCK # anything within a block, on either side, of the hazard impacts the hazard

# Window setup
gw = GWindow(WINDOW,WINDOW)

# ground code here, possibly

# player code here, possibly

# hazard code here, possibly

def tick():
    pass

def jump(e):
    pass

# Event setup
gw.set_interval(tick, TICK_MS)
gw.add_event_listener("click", jump)