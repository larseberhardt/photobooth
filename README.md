# Photobooth Python

Thats a very simple script for a photobooth with a Raspberry PI.
Its also using the gphoto library.

# Function Overview

0. The Monitor shows a Introduction to press the button
1. User press the Button
2. Now starts a countdown of 5 seconds
3. The Camera takes a photo (look at gphoto if your camera is supported)
4. The Photo is shown for few seconds
5. Go back to zero

# Installation

• If you want the the script starts at boot, place the script in your rc.local "sudo python /home/pi/photobooth/photobooth.py &"
• Edit the pictures in the path "img" and save them in the resolution of your monitor
• Be sure that you installed gphoto2 and fbi
• Check if all paths are correct
• Have fun with you photobox on your next BBQ