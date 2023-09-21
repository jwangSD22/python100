from tkinter import *
import time

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30
CHECK = '✔'
POMODORO = 0
BREAK_ACTIVE = False
MINUTES = None
SECONDS = 60


# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# Every time you press the start button it runs the next step 

def startPomodoro():
    global POMODORO
# if pomodoro === 4 && break_active
    # run a 30 min break 
        #set minutes to LONG_BREAK_MIN
        #Countdown(Minutes)
    if(POMODORO == 4 and BREAK_ACTIVE):
        countdown(30)
        
        
    # break_active to false 
    # message to press start to reset pomodoro or hit reset button 
    
# if pomodoro ===4 && ! break_active
    # run timer reset function 

    if (POMODORO < 4 and BREAK_ACTIVE== False):
        countdown(25)
        time.sleep(5)
        POMODORO+=1
        checkmarks = ''
        for _ in range (0,POMODORO):
            checkmarks = checkmarks+CHECK
        checks.config(text = checkmarks)
        
# if pomodoro is less than 4 and break is false 
    # run a 25 min pomodoro
        #set minutes to WORK_MIN
        # Countdown(Minutes)
        
    # add 1 to pomodoro
    # update image for number of pomodoros
    
    # set break_active to true

# if pomodoro is less than 4 and break is True
    # run a 5 min break
        #set minutes to SHORT_BREAK_MIN
        # Countdown (Minutes)
    # set break_active to false
    



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# def countdown(min):
#     minutes = int(min)
#     seconds = 60
    

    
#     time.sleep(1)
#     minutes-=1
#     seconds-=1
    
#     print(type(minutes))
    
#     while(minutes > 0):
#         readout_minutes = ''
#         readout_seconds = ''

#         if seconds == 60:
#             readout_seconds = f'00'
#         elif seconds < 10:
#             readout_seconds = f'0{seconds}'
#         else:
#             readout_seconds = f'{seconds}'
        
#         if minutes<10:
#             readout_minutes = f'0{minutes}'
#         else:
#             readout_minutes = f'{minutes}'
        
#         canvas.itemconfig(canvas_text,text=f'{readout_minutes}:{readout_seconds}')
  
    
#         # time.sleep(1)
#         seconds-=1
#         print(f'seconds here {seconds}')
#         if seconds == 0:
#             minutes-=1
#             seconds = 60
            
            
def countdown(minutes, seconds=0):
    if minutes < 0:
        return  # Prevent negative time
    if seconds < 0:
        minutes -= 1
        seconds = 59

    readout_minutes = f'{minutes:02}'
    readout_seconds = f'{seconds:02}'
    canvas.itemconfig(canvas_text, text=f'{readout_minutes}:{readout_seconds}')

    if minutes == 0 and seconds == 0:
        # Timer has reached zero, handle this event if needed
        return
    else:
        seconds -= 1
        if seconds < 0:
            minutes -= 1
            seconds = 59
        # Call the countdown function again after 1000 milliseconds (1 second)
        window.after(5, countdown, minutes, seconds)

# Example usage:
# countdown(25)  # Start a 25-minute countdown
    

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro Technique')
window.config(padx=100,pady=50, bg = YELLOW)

##Timer label
timer = Label(text='Pomodoro Timer',font=('Courier','24','bold'),bg=YELLOW)
timer.grid(row=0,column=1)


canvas = Canvas(width=204,height=224)
canvas.config(bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
### must specifiy x and y value
canvas.create_image(102,112,image=tomato_img)
canvas_text = canvas.create_text(102,125, text='00:00', fill='white', font=('Courier','24','bold'))
canvas.grid(row=1,column=1)


start = Button(text='Start',command=startPomodoro)
start.grid(row=2,column=0)


checks = Label(text='',fg=GREEN)
checks.grid(row=3,column=1)
checks.config(bg=YELLOW,font=('Courier','30','bold'))




reset = Button(text='Reset')
reset.grid(row=2,column = 2)


window.mainloop()
