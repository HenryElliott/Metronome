import tkinter as tk
import time
import threading
import pygame
import keyboard  

BPM = 25  
interval = 60 / BPM  

pygame.mixer.init()
sound = pygame.mixer.Sound("beep.wav")

is_running = False
exit_flag = False  

def play_metronome():
    global is_running
    while not exit_flag:
        if is_running:
            sound.play()  
            time.sleep(interval)  
        else:
            time.sleep(0.1)  

def visual_metronome():
    root = tk.Tk()
    root.title("Metronome")
    
    root.geometry("300x200")
    root.configure(bg="#2C2F39")  
    root.overrideredirect(True)
    
    frame = tk.Frame(root, bg="#23272A", bd=5)
    frame.place(relwidth=1, relheight=1, relx=0, rely=0)

    label = tk.Label(frame, text="Metronome", font=("Segoe UI", 24), fg="white", bg="#23272A", width=20, height=4)
    label.pack(padx=20, pady=20)

    instruction_label = tk.Label(frame, text="Press Ctrl + Shift + C to start", font=("Segoe UI", 12), fg="white", bg="#23272A")
    instruction_label.pack(padx=20, pady=5)

    offset_x = 0
    offset_y = 0

    def on_drag_start(event):
        global offset_x, offset_y
        offset_x = event.x
        offset_y = event.y

    def on_drag_motion(event):
        x = root.winfo_x() - offset_x + event.x
        y = root.winfo_y() - offset_y + event.y
        root.geometry(f"+{x}+{y}")

    root.bind("<Button-1>", on_drag_start)
    root.bind("<B1-Motion>", on_drag_motion)

    def flash_label():
        while not exit_flag:
            if is_running:
                label.config(bg="#7289DA")  
                root.update_idletasks()
                time.sleep(interval / 2)  
                label.config(bg="#23272A")  
                root.update_idletasks()
                time.sleep(interval / 2)  
            else:
                time.sleep(0.1)  

    threading.Thread(target=flash_label, daemon=True).start()

    root.eval('tk::PlaceWindow %s center' % root.winfo_toplevel())

    root.mainloop()

def toggle_metronome():
    global is_running
    while not exit_flag:
        if keyboard.is_pressed('ctrl+shift+c'):
            is_running = not is_running
            time.sleep(0.5)

sound_thread = threading.Thread(target=play_metronome, daemon=True)
sound_thread.start()

visual_thread = threading.Thread(target=visual_metronome, daemon=True)
visual_thread.start()

keypress_thread = threading.Thread(target=toggle_metronome, daemon=True)
keypress_thread.start()

try:
    while not exit_flag:
        time.sleep(1)
except KeyboardInterrupt:
    exit_flag = True
    print("Exiting...")
