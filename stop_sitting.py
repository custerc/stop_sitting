import ctypes
import random
import time
import playsound


### BEGIN CUSTOMIZABLE SCRIPT SETTINGS

activities = ['push-ups', 'dips', 'inverted rows'] # activities you want to do go here (stick to 3 for now)

rep_counts = [10, 15, 20, 30] # rep count options you want go here

counter_max = 5 # number of activity breaks you want goes here 

seconds_interval = 5 # number of time in seconds between each activity break goes here

sound_file = 'alert.mp3' # your sound file goes here (store in same directory as script, in mp3 or wav format)

### END CUSTOMIZABLE SCRIPT SETTINGS

counter = 0 

def message_box(seconds, sound):
    random_number = random.random()  # set a random number between 0 and 1
   
    random_reps = random.choice(rep_counts) # choose a random number from rep counts
   
    # SET PERCENT CHANCE FOR EACH ACTIVITY
    if random_number <= 0.33:                           #set % chance of first activity
        final_activity = activities[0]
    elif random_number > 0.33 and random_number <= 0.66: #set % chance of second activity
        final_activity = activities[1]
    elif random_number > 0.66:                          #set % chance of third activity
        final_activity = activities[2]
  
    # PLAY THE ALERT SOUND 
    playsound.playsound(sound) # insert your own sound file and directory info here
    
    # CREATE THE MESSAGE BOX POPUP
    MessageBox = ctypes.windll.user32.MessageBoxW
    MessageBox(None, str(random_reps) + " " + final_activity, 'STOP SITTING AND DO SOMETHING', 0)
   
    # COUNT TIMES SCRIPT HAS RUN
    global counter
    counter += 1
    time.sleep(seconds) # interval in seconds between box pop-ups
   
while counter < counter_max:
    message_box(seconds_interval, sound_file)
