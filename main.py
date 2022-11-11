from win32api import GetCursorPos, SetCursorPos
from time import sleep, perf_counter
from sys import argv

loop_hz = 60

loop_delay = 1/loop_hz

# try to use two arguments as acceleration multiplier and friction floats
# if not, try to use "velocity cursor config.txt" file
try:
    acceleration_multiplier = float(argv[1].replace(',', '.'))
    friction = float(argv[2].replace(',', '.'))
except:
    try:
        with open("velocity cursor config.txt", "r") as f:
            acceleration_multiplier = float(f.readline().replace(',', '.'))
            friction = float(f.readline().replace(',', '.'))
    except:
        # default values used when no arguments or config file or they are invalid
        acceleration_multiplier = 0.5  # acceleration multiplier tells how fast cursor accelerates for example 0.5 = half acceleration, 1 = normal acceleration, 2 = double acceleration
        friction = 0.05                # 1 means infinite friction and 0 means no friction 

old_mouse_position = GetCursorPos()
position = list(old_mouse_position)

velocity = [0, 0]
# synthetic mouse relative is storing the mouse movement that was caused by the code so I can separate user movement from code movement
synthetic_mouse_relative = (0, 0)

# calculate friction multiplier using friction
friction_multiplier = 1 - friction

while True:
    try: # check if win32api.GetCursorPos() is not causing error because of for example lock screen
        mouse_position = GetCursorPos()
        
    except:
        pass
    
    else: # if there's no error, run rest of the code
        # calculate position relative to the old position while taking into account mouse movements caused by code
        mouse_relative = (mouse_position[0] - old_mouse_position[0] - synthetic_mouse_relative[0], mouse_position[1] - old_mouse_position[1] - synthetic_mouse_relative[1])

        # add relative mouse movements to the velocity
        if mouse_relative[0] != 0:
            velocity[0] += mouse_relative[0] * acceleration_multiplier
        if mouse_relative[1] != 0:
            velocity[1] += mouse_relative[1] * acceleration_multiplier

        # move virtual mouse position (float) by velocity
        position[0] += velocity[0]
        position[1] += velocity[1]

        # set real mouse position (intiger) to rounded virtual mouse position
        rounded_virtual_position = (int(round(position[0])), int(round(position[1])))
        try: # avoid crash after packing py to exe with py installer because of win32api.SetCursorPos and for example task manager window
            SetCursorPos((rounded_virtual_position[0], rounded_virtual_position[1]))
        except:
            pass
        
        # calculate relative, "synthetic" mouse movement caused by the code
        synthetic_mouse_relative = (rounded_virtual_position[0] - mouse_position[0], rounded_virtual_position[1] - mouse_position[1])

        # multiply virtual mouse velocity by friction multiplier to make the cursor slow down
        if velocity[0] != 0:
            velocity[0] *= friction_multiplier
        if velocity[1] != 0:
            velocity[1] *= friction_multiplier

        old_mouse_position = mouse_position

        # btw I don't know why this code just works for bouncing off the edges of the screen. I coded the velocity sumulation part and it just also worked for bouncing so I didn't change it.
    
    # perfect delay for making loop oscillate exactly at loop_hz frequency, no matter how long does it take to execute the code inside the loop
    sleep(loop_delay - perf_counter() % loop_delay)