# stop_sitting
A short Python script to prompt short exercise breaks while you're working on a Windows PC. It requires Windows with Python 3.7, and the `playsound` module, which you can see documentation for [here](https://pypi.org/project/playsound/), installed.

When run, `stop_sitting.py` will generate an alert sound and a pop-up message in Windows to remind you to do an activity (like an excercise) one time every X number of seconds. It was inspired by the free Windows program [Big Stretch Reminder](http://monkeymatt.com/bigstretch/), which is probably a better option for most people. However, I wanted to create something with similar functionality but even more customizability, like the ability to make messages appear based on probability settings, and the ability to generate messages with random rep counts pulled from a separate list.

Currently `stop_sitting.py`chooses which activity to recommend based on preset probabilities. It's set to 33% chance for each activity occurring, but changing this setting requires making some edits to the `message_box()` function, which is something I plan to improve in a later version.

## What you can customize

At the top of the script are 5 variables that should be easy for anyone to customize.

`activities` is a list of strings, each one representing one activity you'd like to do during a break. At present, this list must contain exactly 3 items unless you're going to make changes inside the the `message_box()` function, but I would like to improve on this in a future version.

`rep_counts` is a list of integers that represent the options you want for each activity's assigned reps. You can include as many entires on this list as you want; one of these entries will be chosen randomly for each activity message that pops up, independent of which activity has been assigned. 

`counter_max` is the number of activity breaks (counting the one that appears instantly when you run the script) you want to have before the script stops running and exits. Default setting is 5, but personally I like to keep this at around 11 or 12 and set breaks to every 45 or 50 minutes.

`seconds_interval` is the number of seconds between each activity break. Default setting is 5 for easy testing purposes, but for actual use while working I'd recommend changing this to something between 2700 (45 minutes) and 3600 (one hour). 

`sound_file` is the name and location of the alert sound file you want played (it must be .mp3 or .wav). Simply put the file into the same directory as the script and then replace `alert.mp3` with _yourfilename.mp3_.

-e "Update: just testing!" 
