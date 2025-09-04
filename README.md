# TimeGuard ⏰

A Python-based **screen-time restriction tool** that helps control computer usage during restricted hours.  
When triggered, the program blocks the screen with a fullscreen window, shows a motivational quote, starts a countdown, and then forces the computer into hibernate or shutdown mode.  
All blocked sessions are logged for review.

---

## ✨ Features
- Restrict PC usage during specific hours.
- Fullscreen blocking window with countdown.
- Random motivational quotes for encouragement.
- Automatic hibernate/shutdown after countdown.
- Logging of each blocked session with timestamp.
- Protection against closing the window with the "X" button.
- (Optional) Auto-start on boot/resume using Task Scheduler.

---

## 📦 Requirements
- Python 3.x
- Tkinter (comes pre-installed with Python)
- Windows OS (uses `shutdown` command)

---

## 📂 Project Structure
Project/
│── main.py # Main script
│── Quote/quote.txt # File containing quotes (one per line)
│── Logs/log_info.log # Log file (created automatically)



---

⚠️ Warning
This script forces shutdown/hibernate.
Make sure to save your work before restricted hours, otherwise unsaved progress will be lost.

📌 License
This project is open-source. You can modify and use it for personal productivity or parental control.


---


