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

yaml
Copy code

---

## ⚙️ Setup & Usage

### 1. Clone or Download
```bash
git clone https://github.com/yourusername/timeguard.git
cd timeguard
2. Add Quotes
Put your motivational quotes in Quote/quote.txt

Example format:

pgsql
Copy code
If you can dream it, you can achieve it. —Zig Ziglar
The future depends on what you do today. —Mahatma Gandhi
3. Run the Script
bash
Copy code
python main.py
If current time matches restricted hours, the block window will appear.

Countdown will start from 5 seconds.

After countdown, the PC will hibernate/shutdown (depending on settings).

🕑 Configuration
Change Restricted Hours
In main.py:

python
Copy code
restricted_time = [20, 21, 22, 23, 0, 1, 2, 3, 4, 5, 6, 7, 8, 12, 13, 14, 18]
These numbers represent hours in 24-hour format.

Example: 20 = 8 PM, 0 = midnight.

Change Shutdown Mode
Inside the countdown function, you can switch between hibernate and shutdown:

python
Copy code
# Hibernate
os.system("shutdown /h")

# OR Shutdown
os.system("shutdown /s /f /t 0")
🔄 Auto-Start on Boot/Resume (Optional)
You can use Task Scheduler to make this script run automatically:

Open Task Scheduler (taskschd.msc).

Create a new task:

Trigger: At logon or On workstation unlock or On resume from sleep.

Action: Run your Python script.

Save.

📜 Logs
Logs are saved in Logs/log_info.log

Example:


2025-09-04 18:05:23 - hibernate because of restricted hours.
⚠️ Warning
This script forces shutdown/hibernate.
Make sure to save your work before restricted hours, otherwise unsaved progress will be lost.

📌 License
This project is open-source. You can modify and use it for personal productivity or parental control.


---

Do you want me to also prepare a **ready-made `quote.txt` file** with 100+ motivational quotes so use
