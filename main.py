from tkinter import *
from tkinter import filedialog, colorchooser

from PIL import Image, ImageDraw, ImageFont
import math

# --- Constants --- #
LIGHT_GREEN ='#00af91'
GREEN = '#007965'
ORANGE = '#f58634'
YELLOW = '#ffcc29'
RATIO = 8
FONT_NAME = 'Courier'
WTM_COLOR = 'white'

def check_size(img):
    width = img.size[0]
    height = img.size[1]
    return width * height

def check_orientation(img):
    width = img.size[0]
    height = img.size[1]
    if width > height:
        return 'horizontal'
    elif width == height:
        return 'square'
    else:
        return 'vertical'


def upload_action(event=None):
    filename = filedialog.askopenfilename()
    print('Selected:', filename)
    img = Image.open(filename)
    # img.show()
    img.save('./images/img.png')
    action_txt_lbl.grid(row=2, column=0)
    wtm_text_btn.grid(row=2, column=1)
    action_logo_txt.grid(row=3, column=0)
    wtm_logo_btn.grid(row=3, column=1)


def wtm_text_dialogue():
    action_logo_txt.grid(row=4, column=0)
    wtm_logo_btn.grid(row=4, column=1)
    wtm_text_entry.grid(row=3, column=0)
    color_btn.grid(row=3, column=1)
    submit_wtm_txt.grid(row=3, column=2)
    # wtm_text_dialogue.focus()


def wtm_text():
    img = Image.open('./images/img.png')
    text = wtm_text_entry.get()
    image_text = img.copy()
    drawing = ImageDraw.Draw(image_text)
    font = ImageFont.truetype("../Library/Fonts/Courier New.ttf", 40)
    drawing.text((10, 10), text, fill=WTM_COLOR, font=font)
    image_text.show()
    image_text.save('./images/img.png')


def wtm_logo():
    filename = filedialog.askopenfilename()
    print('Selected:', filename)
    logo = Image.open(filename)
    img = Image.open('./images/img.png')
    if check_size(logo) > check_size(img)/RATIO:
        logo.thumbnail((img.size[0]/RATIO, img.size[1]/RATIO))
        logo.save('./images/logo_thumbnail.png')
    image_logo = img.copy()
    position = ((image_logo.width - logo.width), (image_logo.height - logo.height))
    image_logo.paste(logo, position, logo)
    image_logo.save('images/img.png')
    image_logo.show()

def color_chooser():
    global WTM_COLOR
    WTM_COLOR = colorchooser.askcolor(parent=window,
                                             initialcolor=(255, 0, 0))[1]

# --- UI --- #
window = Tk()
window.title("Watermarkme")
window.config(padx=100, pady=100, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

# Labels
title_label = Label(text="WatermarkMe", font=(FONT_NAME, 48, "normal"), bg=YELLOW, fg=GREEN)
title_label.grid(column=0, row=0, columnspan=2)
upload_lbl = Label(text="Pick a picture to watermark", font=('Calibri', 24, "normal"), bg=YELLOW, fg=ORANGE, padx=15)
upload_lbl.grid(column=0, row=1)

# Buttons
upload_btn = Button(text='Upload', highlightthickness=0, command=upload_action, bg=YELLOW)
upload_btn.grid(column=1, row=1)
action_txt_lbl = Label(text="What's the text you want to watermark on your picture?",
                           font=('Calibri', 16, "normal"), bg=YELLOW, fg=LIGHT_GREEN, padx=15)
action_logo_txt = Label(text="What's the logo you want to watermark on your picture?",
                        font=('Calibri', 16, "normal"), bg=YELLOW, fg=LIGHT_GREEN, padx=15)
wtm_text_btn = Button(text='Type', highlightthickness=0, command=wtm_text_dialogue)
wtm_logo_btn = Button(text='Upload Logo', highlightthickness=0, command=wtm_logo)
submit_wtm_txt = Button(text='Submit', highlightthickness=0, command=wtm_text)
color_btn = Button(text="Color", highlightthickness=0, command=color_chooser)

# Entries
wtm_text_entry = Entry(width='35')

window.mainloop()