import datetime
import tkinter as tk
import random
import os


restricted_time = [20,21,22,23,00,1,2,3,4,5,6,7,8,12,13,14,19] # the hour where i want pc should be shutdown

# ================================================================================
def block_run():
        # os.system("shutdown /h")
        print("Hibernated")
# ====================================================================================
def gui():
    print("Gui Run")  
    colors = ["Red","Blue","Green","Yellow","White"]
    root = tk.Tk()
    root.protocol("WM_DELETE_WINDOW", block_quit)
    root.attributes("-fullscreen", True) 
    root.configure(bg="Black")
    root.attributes("-alpha", 0.9) 
        # ------------- count text configuration ---------------------
    counter_value = 5
    count_text = tk.Label(root, font=("Arial",59))
    count_text.pack(expand=True,anchor="center")
        # ----------- this gonna count from 5 to 0 ------------
    def count():
        nonlocal counter_value
        if counter_value >= 0:
            count_text.configure(bg="Black",fg= random.choice(colors))
            count_text.config(text=(str(counter_value)))
            counter_value -= 1
            root.after(1000,count)
            if counter_value == -1:
                log_info()
                root.destroy()
                block_run()
    # ----------------------------- Quote Text ---------------------
    with open("Quote/quote.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
    random_choice = random.choice(lines).strip()
    quote_text = tk.Label(root,text=random_choice,font=("Arial",30),wraplength=1000,justify="center",bg="Black",fg="white")
    quote_text.pack(anchor="center",expand=True)
    count()
        
    root.mainloop()

# ======================================================================================================
def log_info():
    with open("Logs/log_info.log","a") as f:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{timestamp} - hibernate because of restricted hours.\n")
# ========================================================================
def main():
    print("mainScript Run")
    time_now = datetime.datetime.now().hour
    if time_now in restricted_time:
        gui()
# ===============================================================================
def block_quit():
    None
# ====================================================================
if __name__== "__main__":
    main()
