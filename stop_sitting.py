import ctypes
import random
import time
import playsound

activities = ['push-ups', 'dips', 'inverted rows'] # messages that appear in the pop-up

rep_counts = [10, 15, 20, 30] # rep counts for exercises you want to do

counter = 0

def message_box():
    random_number = random.random()  # set a random number between 0 and 1
   
    random_reps = random.choice(rep_counts) # choose a random number from rep counts
   
    # SET PERCENT CHANCE FOR EACH ACTIVITY
    if random_number <= 0.33:                           #set % chance of first message
        final_activity = activities[0]
    elif random_number > 0.33 and random_number <= 0.66: #set % chance of second message
        final_activity = activities[1]
    elif random_number > 0.66:                          #set % chance of third message
        final_activity = activities[2]
  
    # PLAY THE ALERT SOUND 
    playsound.playsound('alert.mp3')
    
    # CREATE THE MESSAGE BOX POPUP
    MessageBox = ctypes.windll.user32.MessageBoxW
    MessageBox(None, str(random_reps) + " " + final_activity, 'STOP SITTING AND DO SOMETHING', 0)
   
    # COUNT TIMES SCRIPT HAS RUN
    global counter
    counter += 1
    time.sleep(5) # interval in seconds between box pop-ups
   
while counter < 5:
    message_box()