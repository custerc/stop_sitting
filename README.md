# stop_sitting
A short Python script to prompt short exercise breaks

This is a Python script that will generate a pop-up message in Windows to remind you to do an activity (like an excercise) once every so often. I created it because while solutions exist for this, I wanted one that would let me customize the probabilities each exercise would come up.

It chooses which activity to recommend based on preset probabilities, and assignes a number of reps at random from a preset list of rep counts.

It should be fairly easy to customize with basic Python skills.

`activities` is a list, you can list the activities/exercises you want prompted here.

`rep counts` is another list, for the list of rep count options you want `stop_sitting.py` to choose from.

`message_box()` is the function that selects a rep count at random, selects an activity based on a random number and probability settings (currently set to 33% for each), creates the pop-up message, and then sleeps the script for a set period of time in seconds.

`counter` is what I'm using to limit the number of times the script runs before finishing. Setting a max of 10-12 should get you through the average work day. There's almost certainly a much better way to do this, but I don't know it yet, so there you have it.

In the future I intend to add an alert sound that accompanies the message pop-up, and I have tried to use the `playsound` module for this, but it's not working in the current version of this script so it's commented out.
