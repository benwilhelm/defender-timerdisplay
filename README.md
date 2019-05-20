# Headless Timer Display for Launch Timer Video Feed

## What's this

This is a python app that runs in xterm, allowing us to send a display of the launch timer to the video computer to be mixed into the big board display. It replaces the web based version so that it can be configured to run on boot without a keyboard or mouse attached to the pi.

## Installation

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Running from the command line 

Following [this tutorial](https://www.raspberrypi.org/forums/viewtopic.php?t=152264), create a file called `starttimer` in your root directory, and put this in it:

```
#!/bin/sh
openbox --config-file ~/.config/openbox/rc.xml --startup /path/to/defender-timerdisplay/start
```

Then run the app with `xinit ./starttimer` 

## MAJOR known issue 

We have not yet figured out how to keep the Raspberry Pi from going to sleep. This will be critical to solve so that the launch timer doesn't disappear from the big board after 15 minutes
