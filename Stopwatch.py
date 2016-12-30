# "Stopwatch: The Game"

# tenth of a second between every tick
# every time timer ticks, it will update a global variable by one

import simplegui

# define global variables
time = 0
success = 0
attempts = 0
counter = 0
# variable to ensure score can only be increased after stopwatch was running
stopwatch_running = False


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    a_time = t // 600
    b_time = ((t / 10) % 60) // 10
    c_time = ((t / 10) % 60) % 10
    d_time = t % 10
    return str(a_time) + ":" + str(b_time) + str(c_time) + "." + str(d_time)


# define event handlers for buttons; "Start", "Stop", "Reset"
def button_start():
    stopwatch_timer()

def button_stop():
    timer.stop()
    global success, attempts, stopwatch_running
    if stopwatch_running == True:
        if (time % 10) == 0:
            success += 1
            attempts += 1
        else:
            attempts += 1
    else:
        return        
    stopwatch_running = False
    
def button_reset():
    global time, success, attempts
    time = 0
    success = 0
    attempts = 0
    return time, success, attempts


# define event handler for timer with 0.1 sec interval
# stopwatch timer event handler
def stopwatch_timer():
    timer.start()
    global time, stopwatch_running
    time += 1
    stopwatch_running = True
    return time, stopwatch_running
    

# define draw handler
def draw_handler(canvas):
    # stopwatch display on canvas
    canvas.draw_text(format(time), [90, 140], 50, "White")
    # score display
    canvas.draw_text(str(success) + "/" + str(attempts), [220, 50], 25, "Red")

    
# create frame
frame = simplegui.create_frame("Stopwatch: The Game", 300, 200)

# register event handlers
timer = simplegui.create_timer(100, button_start)
start = frame.add_button("Start", button_start, 100)
stop = frame.add_button("Stop", button_stop, 100)
reset = frame.add_button("Reset", button_reset, 100)
frame.set_draw_handler(draw_handler)

# start frame
frame.start()
