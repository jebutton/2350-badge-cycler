# 2350-badge-cycler
An alternative take on the Tufty 2350 vendor-supplied badge demo that allows for multiple identities to be cycled. 
Intended for IRL event use at conferences and the like where you might need to have two or more different identities quickly accessible.
Written in MicroPython.

## Supported Hardware / OS Versions
This is an app for the Pimoroni Badgewear Tufty 2350.  You can buy it at: https://shop.pimoroni.com/en-us/products/tufty-2350.  
It was developed under **device firmware version 3.1.1**  
You can check out more programming related information and get firmware builds at: https://github.com/pimoroni/tufty2350.

## Instructions for first use
1. Update your Tufty 2350 to firmware version 3.1.1 (or else the code won't work).
2. Press the reset button twice on the back of your 2350 to mount it in storage mode.
3. Copy the *badge-cycler* folder from this repo to your /apps/ folder on your device.
4. Eject your device (there is an error, but ignore it).
5. Navigate in your device to the badge-cycler app and start it and see what it looks like.

## Adding your own identities
If you're not looking to extend the capabilities of the program,
you can add your own identities to the badge by editing the *badge_profiles.json* file.
The *badge_profiles.json* file is where the identities are stored. It is simply a JSON file that allows you to specify what you want to be displayed for each identities.   
It must obey JSON syntax.  
Every line accepts ASCII strings except for *background_color* and *header_text_color* which requires 3 integer values for Red, Green, and Blue.
- *background_color* is the background color for the first and last rows of the badge.
- *header_text_color* is the font color for the text that is in the lines covered by *background_color*.

To add an avatar, it must be done as follows:
1. Resize / Reformat the image to a 100px x 100px png.
2. Place the image in */badge-cycler/avatars/*
3. Edit the *id_photo* value in that identity's JSON entry to have the format: *"/system/apps/badge-cycler/assets/avatars/name_of_avatar_file.png"*  

After you create a new identity, repeat steps 2-5 of the Instructions for first use to update the app on your device.

## How to use the app
Once you've launched the app from the device's built in OS, you can navigate through your identities by using the up and down buttons.

New: Use the "A" and "B" Buttons to switch between the original passport-like mode to a simplified mode with just the name and a larger avatar.
