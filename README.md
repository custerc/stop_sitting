# stop_sitting
A short Python script to prompt short exercise breaks

This is a Python script that will generate a pop-up message in Windows to remind you to do an activity (like an excercise) once every so often. I created it because while solutions exist for this, I wanted one that would let me customize the probabilities each exercise would come up.

It chooses which activity to recommend based on preset probabilities, and assignes a number of reps at random from a preset list of rep counts.

It should be fairly easy to customize with basic Python skills.

`activities` is a list, you can list the activities/exercises you want prompted here.

`rep counts` is another list, for the list of rep count options you want `stop_sitting.py` to choose from.

`message_box()` is the function that selects a rep count at random, selects an activity based on a random number and probability settings (currently set to 33% for each), creates the pop-up message, and then sleeps the script for a set period of time in seconds. 

`counter` is what I'm using to limit the number of times the script runs before finishing. How many times you want it to run depends on your time interval between messages (see below) but in general you probably want to keep the number in `while counter > 5` to under 30. There's almost certainly a much better way to do this, but I don't know it yet, so there you have it.

Edit the number of seconds im `time.sleep(5)` to change how frequently the messages appear in seconds. In this script on GitHub the default is 5 for testing purposes, but my personal preference for actual use is 3000 seconds, which is every 50 minutes.

