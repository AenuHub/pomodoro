from tkinter import *
import winsound  # Use winsound for playing sound on Windows

# CONSTANTS
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1 / 2
SHORT_BREAK_MIN = 1 / 3
LONG_BREAK_MIN = 1
REPS = 0
timer = None

# --- TIMER RESET --- #

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer")
    checkmark.config(text="")
    global REPS
    REPS = 0

# --- TIMER MECHANISM --- #

def start_timer():
    global REPS
    REPS += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if REPS % 8 == 0:
        countdown(long_break_sec)
        label.config(text="Break", fg=RED)
    elif REPS % 2 == 0:
        countdown(short_break_sec)
        label.config(text="Break", fg=PINK)
    else:
        countdown(work_sec)
        label.config(text="Work", fg=GREEN)

# --- COUNTDOWN MECHANISM --- #

def countdown(count):
    minutes = int(count) // 60
    seconds = int(count) % 60
    # formats the time in minutes and seconds as MM:SS
    canvas.itemconfig(timer_text, text=f"{minutes:02d}:{seconds:02d}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        play_sound()
        start_timer()
        marks = ""
        work_sessions = REPS // 2
        for _ in range(work_sessions):
            marks += "✔"
        checkmark.config(text=marks)

def play_sound():
    winsound.Beep(1000, 500)

# --- UI SETUP --- #

window = Tk()
window.geometry("500x500")  # Set a static size for the window
window.config(padx=110, pady=70, bg=YELLOW)
window.title("Pomodoro Counter")
window.resizable(False, False)

label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
label.grid(column=1, row=0)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

checkmark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 14, "bold"))
checkmark.grid(column=1, row=3)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Prevent window from expanding when widgets are updated
window.grid_propagate(False)

window.mainloop()