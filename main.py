from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

current_card = {}

try:
  with open('python_tut/day31/flash-card-project-start/data/to_learn.csv') as file:
    data = pandas.read_csv(file)
except FileNotFoundError:
  with open('python_tut/day31/flash-card-project-start/data/french_words.csv') as file:
    data = pandas.read_csv(file)
finally:
  data_dict = data.to_dict(orient='records')
  
def right_button_clicked():
  data_dict.remove(current_card)
  data_to_save = pandas.DataFrame(data_dict)
  data_to_save.to_csv('python_tut/day31/flash-card-project-start/data/to_learn.csv', index=False)
  next_word()
  
def wrong_button_clicked():
  next_word()

def next_word():
  global current_card, flip_timer
  window.after_cancel(flip_timer)
  current_card = random.choice(data_dict)
  canvas.itemconfig(word, text=current_card['French'], fill='black')
  canvas.itemconfig(title, text='French', fill='black')
  canvas.itemconfig(background, image=card_front_img)
  flip_timer = window.after(3000, func=flip_card)
  
def flip_card():
  canvas.itemconfig(title, text='English', fill='white')
  canvas.itemconfig(word, text=current_card['English'], fill='white')
  canvas.itemconfig(background, image=card_back_img)
  
window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

card_back_img = PhotoImage(file='python_tut/day31/flash-card-project-start/images/card_back.png')
card_front_img = PhotoImage(file='python_tut/day31/flash-card-project-start/images/card_front.png')
canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
background = canvas.create_image(400, 263, image=card_front_img)
title = canvas.create_text(400, 150, text='', font=('Arial', 40, 'italic'))
word = canvas.create_text(400, 263, text='', font=('Arial', 60, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)

wrong_img = PhotoImage(file='python_tut/day31/flash-card-project-start/images/wrong.png')
right_img = PhotoImage(file='python_tut/day31/flash-card-project-start/images/right.png')
wrong_button = Button(image=wrong_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=wrong_button_clicked)
wrong_button.grid(row=1, column=0)
right_button = Button(image=right_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=right_button_clicked)
right_button.grid(row=1, column=1)

next_word()

window.mainloop()


