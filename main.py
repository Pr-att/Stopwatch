from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1 * 60
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
start = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset():
    window.after_cancel(start)
    canvas.itemconfig(count_text, text=f'00:00', font=(FONT_NAME, 20, 'bold'), fill='white')

# ---------------------------- TIMER MECHANISM ------------------------------- #


def count_down(count=WORK_MIN):

    count_min = math.floor(count / 60)
    count_sec = round(count % 60)
    if count_sec < 10:
        count_sec = f'0{count_sec}'
    if count >= 0:
        canvas.itemconfig(count_text, text=f'{count_min}:{count_sec}')
        global start
        start = window.after(1000, count_down, count - 1)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


counts_min = math.floor(WORK_MIN / 60)
counts_sec = round(WORK_MIN % 60)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro')
window.config(bg=YELLOW)

canvas = Canvas(width=440, height=448, bg=YELLOW)
img = PhotoImage(file='tomato.png')
canvas.create_image(220, 224, image=img)
count_text = canvas.create_text(220, 240, text=f'00:00', font=(FONT_NAME, 20, 'bold'), fill='white')


canvas.pack()

# Label
label = Label(text='TIMER', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, 'bold'))
label.place(x=150, y=40)

# buttons
b1 = Button(text='Start', fg=PINK, font=(FONT_NAME, 10), command=count_down)
b1.place(x=80, y=350)

b2 = Button(text='Reset', fg=PINK, font=(FONT_NAME, 10), command=reset)
b2.place(x=300, y=350)

check_mark = Label(text='✔', bg=YELLOW)
check_mark.place(x=215, y=380)


window.mainloop()