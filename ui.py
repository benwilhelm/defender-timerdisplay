import sys
from tkinter import *
from skt import sio
import signal

app = None

@sio.on('tick')
def on_tick(evt):
    if app:
        app.update_time(evt['timeToLaunch'])


class Fullscreen_Window:

    def __init__(self):
        self.tk = Tk()
        self.tk.protocol("WM_DELETE_WINDOW", close_app)
        # self.tk.attributes('-topmost', True)
        self.tk.attributes('-fullscreen', True)
        self.tk.configure(bg='black')

        self.frame = Frame(self.tk)
        self.frame.configure(cursor='none')
        self.frame.pack()

        self.label = Label(
            self.frame,
            text="60:00",
            font=("Courier", 150),
            fg="white",
            bg="black",
            pady=100
        )
        self.label.pack()

        self.state = True
        # self.tk.bind("<F11>", self.toggle_fullscreen)
        self.tk.bind("<Escape>", self.toggle_fullscreen)

    def toggle_fullscreen(self, event=None):
        self.state = not self.state
        self.tk.attributes('-fullscreen', self.state)
        return "break"

    def end_fullscreen(self, event=None):
        self.state = False
        self.tk.attributes('-fullscreen', False)
        return "break"

    def update_time(self, time):
        disp = secToDisplay(time)
        self.label.configure(text=disp)


def start():
    global app
    if app == None:
        app = Fullscreen_Window()
        app.tk.mainloop()
    return app

def close_app(sig=None, frame=None):
    sio.disconnect()
    app.tk.destroy()

def secToDisplay(t):
    seconds = int(t % 60)
    minutes = int(t / 60)

    s_ones = int(seconds % 10)
    s_tens = int(seconds / 10)

    m_ones = int(minutes % 10)
    m_tens = int(minutes / 10)

    return str(m_tens) + str(m_ones) + ':' + str(s_tens) + str(s_ones)

signal.signal(signal.SIGINT, close_app)
