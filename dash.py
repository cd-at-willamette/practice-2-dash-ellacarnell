from pgl import *

# Constants
WINDOW = 400 # This is the width and height of the game window
TICK_MS = 200 # This is how often the tick function is called, in milleseconds this controls the game speed

# Derived Constants
BLOCK = WINDOW / 10
GROUND = WINDOW - BLOCK
GRAVITY = BLOCK / 4
FLOOR = GROUND - BLOCK # Blocks need to be placed block height above the ground to be on the floor.
DANGER = 3 * BLOCK # anything within a block, on either side, of the hazard impacts the hazard

# Window setup
gw = GWindow(WINDOW,WINDOW)  # This is the creates the window

gw.add(GLine(0, GROUND, WINDOW, GROUND)) # (x1, y1, x2, y2)

player = GRect(BLOCK, BLOCK)  # (width, height)
player.set_filled(True)
player.set_fill_color("lavender")
gw.add(player, BLOCK, FLOOR) # place the player one block from the left sitting on the floor 


vy = 0 # This is the vertical velocity 
air = False # Whether the player is currently in the air (mid jump)


# hazard code here, possibly
hazard = GRect (BLOCK, BLOCK) # creates the hazard that has width block and height block
hazard.set_filled(True)
hazard.set_fill_color("orange")
gw.add(hazard, WINDOW, FLOOR) # places the hazard that off screen on the right 
gw.vx = BLOCK # this is the horizontal movement speed of the hazard and it moves to the left with each tick 
gw.score = 0

def tick():
    global vy, air # This declares that we are modifying air and vy

    if not air and hazard.get_x() < DANGER: # this is collision detection if the player is too close to the hazard and not jumping 
        exit(print("Game Over", gw.score)) # End program after printing game over

    new_x = hazard.get_x() -gw.vx # This section moves the hazard to the left. This line subtract speed from current x-position
    if new_x < 0: # If hazard has moved past the left edge of the window 
        new_x = WINDOW # hazard moved back to the right edge of the window 
        gw.score += 1
    hazard.set_location(new_x, FLOOR) # updates hazards position on the screen 


    if air: # These lines handle the jumping motion if the player is in the air
        new_y = player.get_y() - vy # moves the player up or down depending on velocity 
        vy -= GRAVITY # applies gravity reducing the vertical velocity each tick 
        if new_y >= FLOOR: # if the player lands back on the floor
            new_y = FLOOR # Reset player to exactly floor level
            air = False  # player is no longer jumping 
        player.set_location(BLOCK, new_y) # updates vertical position of player on the screen 

def jump(e): # this is the jumping function that is called when the event occurs. The event occuring in this context is the click 
    global air, vy # uses the global values for air and vy
    if not air: # only allows jumping if the player isn't already in the air 
        vy = BLOCK # This provides the upward velocity to start the jump 
        air = True # This marks the player as jumping 

# Event setup
gw.set_interval(tick, TICK_MS) # This runs the tick function automatically tick_ms milleseconds 
gw.add_event_listener("click", jump) # This calls the jump function every time a click is observed
