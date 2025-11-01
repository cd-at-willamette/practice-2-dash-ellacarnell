from pgl import *

# Constants
WINDOW = 400
TICK_MS = 100

# Derived Constants
BLOCK = WINDOW / 10
GROUND = WINDOW - BLOCK
GRAVITY = BLOCK / 4
FLOOR = GROUND - BLOCK # Blocks need to be place block height above the ground to be on the floor.
DANGER = 3 * BLOCK # anything within a block, on either side, of the hazard impacts the hazard

# --- Window Setup ---
gw = GWindow(WINDOW,WINDOW)

# Ground line
gw.add(GLine(0, GROUND, WINDOW, GROUND))

# player
gw.me = GRect(BLOCK,BLOCK)
gw.air = False
gw.vy = 0
gw.gravity = GRAVITY
gw.me.set_fill_color("hot pink")
gw.me.set_filled(True)
gw.add(gw.me, BLOCK, FLOOR)

# hazard
gw.hz = GRect(BLOCK,BLOCK)
gw.vx = BLOCK
gw.hz.set_fill_color("olive drab")
gw.hz.set_filled(True)
gw.add(gw.hz, WINDOW, FLOOR)
gw.score = 0

def tick():
    # collision check
    if not gw.air and gw.hz.get_x() < DANGER:
            exit(print("Rip:", gw.score))

    # move hazard
    new_x = gw.hz.get_x() - gw.vx
    if new_x < 0:
        new_x = WINDOW
        gw.score += 1
    gw.hz.set_location(new_x, FLOOR)

    # jump physics
    if gw.air:
        # Change location
        new_y = gw.me.get_y() - gw.vy
        gw.me.set_location(BLOCK, new_y)
        # Change momentum
        gw.vy -= gw.gravity
        if new_y >= FLOOR:
            gw.air = False
            gw.me.set_location(BLOCK, FLOOR)

def jump(e):
    if not gw.air:
        gw.vy = BLOCK
        gw.air = True

# --- Events ---
gw.set_interval(tick, TICK_MS)
gw.add_event_listener("click", jump)