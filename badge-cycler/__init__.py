import sys
import os
import json
from collections import OrderedDict
sys.path.insert(0, "/system/apps/badge-cycler")
os.chdir("/system/apps/badge-cycler")

class BadgeInstance:
    """ A class that holds the data for a single badge.
    """
    def __init__(self, json_dict):
        screen.antialias = screen.X2

        # details to be shown on the card
        try:
            self.id_photo_small = image.load(json_dict['id_photo'], 50, 50)
            self.id_photo_large = image.load(json_dict['id_photo'], 72, 72) 
        except:
            self.id_photo_small = image.load("/system/apps/badge-cycler/assets/avatars/blank_avatar_lg.png", 50, 50)
            self.id_photo_large = image.load("/system/apps/badge-cycler/assets/avatars/blank_avatar_lg.png", 72, 72) 
        self.id_name = json_dict['id_name']
        self.id_title = json_dict['id_title']

        self.background = color.rgb(json_dict['background_color'][0], json_dict['background_color'][1], json_dict['background_color'][2])
        self.name_text_color = color.rgb(json_dict['header_text_color'][0], json_dict['header_text_color'][1], json_dict['header_text_color'][2])
        self.value_1 = json_dict['value_1']
        self.value_2 = json_dict['value_2']
        self.value_3 = json_dict['value_3']
       
info_font = font.load("/system/assets/fonts/MonaSans-Medium.af")
name_font = font.load("/system/assets/fonts/DynaPuff-Medium.af")

# Get a dictionary badges based on the json file.
with open("badge_profiles.json") as f:
    data_from_file = json.load(f)
f.close()
badge_dict = OrderedDict((i["id_name"], BadgeInstance(i)) for i in data_from_file["badges"])

screen.antialias = screen.X2
index = 0
mode = "A"
current_badge = list(badge_dict.values())[0]

def correct_mode():
    """ A check to make sure the mode doesn't enter a failing state.
    """
    global mode
    if mode not in ["A", "B"]:
        mode = ["A"]

def mode_a_name_display_size(text):
    header_text_size = 25
    text_length = len(text)
    if text_length > 10:
        extra_length = len(text[10:text_length])
        return (header_text_size - (extra_length * 2 ) - 2)
    else:
        return header_text_size
        
def init():
    pass

def on_exit():
    pass


def display_mode_a():
    """ Default mode for display.
    Displays a table-like display with several informational rows.
    """
    global badge_dict, current_badge, index, name_font, info_font
        
    screen.clear()
    header_height = 54
    header_text_x = 56
    header_text_y = 0
    name_text_bounds = rect(header_text_x, header_text_y, screen.width - header_text_x, header_height)
    #header_text_size = 25
    
    info_height = 16
    info_start_x = 0
    info_start_y = header_height
    info_divider_width = 1
    info_text_size = 15

    white = color.rgb(255, 255, 255, 255)
    name_bg_color =  current_badge.background
    name_text_color = current_badge.name_text_color
    divider_color = color.rgb(5, 5, 5, 255)

    # badge header bg
    screen.pen = name_bg_color #color.rgb(10, 10, 10, 250)
    screen.rectangle(0, 0, 320, header_height)
    
    # icon & placeholder
    screen.pen = white
    screen.rectangle (2,2, 50, 50)
    screen.font = name_font
    screen.pen = name_text_color
    picture_x = 2
    picture_y = 2
    
    # Draw Icon
    screen.blit(current_badge.id_photo_small, vec2(picture_x, picture_y))
    
    # Display Badge Name
    screen.text(current_badge.id_name, name_text_bounds, mode_a_name_display_size(current_badge.id_name), align=(image.LEFT, image.MIDDLE))
    
    # BG for socials / title
    screen.pen = white
    screen.rectangle(0, header_height, 320, 240 - header_height)
    
    # Dividing line for header / title
    screen.pen = divider_color
    screen.font = info_font
    screen.rectangle(info_start_x, info_start_y, 320, info_divider_width)
    screen.text(current_badge.id_title,info_start_x, info_start_y, info_text_size)
    
    # Dividing line for title / 1st value
    info_start_y += info_height
    screen.rectangle(info_start_x, info_start_y, 320, info_divider_width)
    screen.text(current_badge.value_1, info_start_x, info_start_y, info_text_size)
    
    # Diving line for 1st and 2nd value
    info_start_y += info_height
    screen.rectangle(info_start_x, info_start_y, 320, info_divider_width)
    screen.text(current_badge.value_2, info_start_x, info_start_y, info_text_size)

    # 3rd Value Section
    info_start_y += info_height
    screen.rectangle(info_start_x, info_start_y, 320, info_divider_width)
    info_start_y += 1

    screen.pen = name_bg_color
    screen.rectangle(info_start_x, info_start_y , 320, screen.height)
    screen.pen = name_text_color
    screen.text(current_badge.value_3, info_start_x, info_start_y, info_text_size)



def display_mode_b():
    """ Second mode for display.
    Displays a larger icon and just display the name, centered.
    Intended for more long-distance readability.
    """
    global badge_dict, current_badge, index, name_font, info_font
        
    screen.clear()
    
    # Set Colors and Fonts
    img_bg_color = color.rgb(248, 248, 255, 255)
    name_bg_color =  current_badge.background
    name_text_color = current_badge.name_text_color
    divider_color = color.rgb(5, 5, 5, 200)
    screen.font = name_font
    
    #Set Coordinates
    img_side = 72
    img_start_y = 2
    img_start_x = (screen.width  / 2) - (img_side / 2)


    name_start_x = 0
    name_start_y = img_start_y + 2 + img_side
    name_height = 160
    name_width = screen.width - (name_start_x * 2)
    name_text_bounds = rect(name_start_x, name_start_y, name_width, 40)
    header_text_size = 25

    # Draw BG rectangle
    screen.pen = img_bg_color
    screen.rectangle(0, 0, screen.width, screen.height)

    # Draw image BG box
    screen.pen = img_bg_color
    screen.rectangle(img_start_x, img_start_y, img_side, img_side)

    # Draw image
    screen.blit(current_badge.id_photo_large, vec2(img_start_x, img_start_y))
    
    # Draw name box
    screen.pen = name_bg_color
    screen.rectangle(name_start_x, name_start_y, name_width, name_height)

    # Print the Badge Name
    screen.pen = name_text_color
    screen.text(current_badge.id_name, name_text_bounds, header_text_size, align=(image.CENTER, image.MIDDLE))

def update():
    global mode, badge_dict, current_badge, index, name_font, info_font

    correct_mode() # set the mode if it hasn't been set

    if mode == "A":
        display_mode_a() # Default original display.

    if mode == "B":
        display_mode_b() # Bigger icon and just the name.

    # Switch mode to default mode
    if badge.pressed(BUTTON_A):
      mode = "A"

    # Switch mode to alternate mode
    if badge.pressed(BUTTON_B):
      mode = "B"

    # Display the previous badge.
    if badge.pressed(BUTTON_DOWN) and index > 0:
      index -= 1
      current_badge = list(badge_dict.values())[index]

    # Display the next badge.
    if badge.pressed(BUTTON_UP) and index < len(badge_dict) - 1:    
      index += 1
      current_badge = list(badge_dict.values())[index]

run(update)
