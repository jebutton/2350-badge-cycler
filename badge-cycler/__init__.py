import sys
import os
import math
import json
from collections import OrderedDict
sys.path.insert(0, "/system/apps/badge-cycler")
os.chdir("/system/apps/badge-cycler")

class BadgeInstance:
    
    def __init__(self, json_dict):
        screen.antialias = screen.X2

        # details to be shown on the card
        try:
            self.id_photo = image.load(json_dict['id_photo']) #imvalue_3.load(json_dict['id_photo'])
        except:
            self.id_photo = image.load("/system/apps/badge-cycler/assets/avatars/blank_avatar.png")
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
current_badge = list(badge_dict.values())[0]

def init():
    pass

def on_exit():
    pass

def update():
    global badge_dict, current_badge, index, name_font, info_font
    
    screen.clear()
    header_height = 54
    header_text_x = 56
    header_text_y = 12
    header_text_size = 25
    
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
    picture_size = 50
    
    # draw icon
    screen.blit(current_badge.id_photo, vec2(picture_x, picture_y))
    
    # Badge Name
    screen.text(current_badge.id_name, header_text_x , header_text_y,header_text_size)
    
    # bg for socials / title
    screen.pen = white
    screen.rectangle(0, header_height, 320, 240 - header_height)
    
    # dividing line for header / title
    screen.pen = divider_color
    screen.font = info_font
    screen.rectangle(info_start_x, info_start_y, 320, info_divider_width)
    screen.text(current_badge.id_title,info_start_x, info_start_y, info_text_size)
    
    # dividing line for title / 1st value
    info_start_y += info_height
    screen.rectangle(info_start_x, info_start_y, 320, info_divider_width)
    screen.text(current_badge.value_1, info_start_x, info_start_y, info_text_size)
    
    # diving line for 1st and 2nd value
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
     
    if badge.pressed(BUTTON_DOWN) and index > 0:
      index -= 1
      current_badge = list(badge_dict.values())[index]

    if badge.pressed(BUTTON_UP) and index < len(badge_dict) - 1:    
      index += 1
      current_badge = list(badge_dict.values())[index]

run(update)
