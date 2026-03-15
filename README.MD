# 🚀 Freelancer API Job Scraper & Telegram Notifier

A robust, multi-threaded Python application that automatically scrapes the Freelancer.com API for new job postings based on your keywords and notifies you instantly via a Telegram Bot. 

Never miss a relevant project again, and stay ahead of the competition without constantly refreshing your browser.

---

## 🏗️ How it Works (Under the Hood)

This project employs a decoupled, asynchronous architecture using Python's `threading` module to run two core processes concurrently:

| Component | Responsibility | Process |
| :--- | :--- | :--- |
| **Scraper** | Polls the Freelancer API, filters jobs, and logs new ones. | Runs on a continuous loop in a background thread. |
| **Listener** | Monitors the log file and dispatches alerts to Telegram. | Acts as an asynchronous event handler in another thread. |

---

## ✨ Features

- **Automated API Scraping:** Efficiently queries the official Freelancer.com API.
- **Deduplication:** Keeps a local state in memory to ensure you are never notified about the same job twice.
- **Real-Time Notifications:** Delivers formatted job details directly to your personal Telegram chat or channel.
- **Modular Core:** A clean code structure with all essential logic organized within the `core/` package.
- **Manual Testing Mode:** For developers! Directly add jobs to the `jobs.txt` file to test the Telegram bot's notifications.

---

## 🛠️ Prerequisites

Before you begin, ensure you have the following:

- **Python:** Version 3.8 or higher.
- **Telegram:** A Bot Token and your personal Chat ID (talk to [BotFather](https://t.me/botfather)).
- **Freelancer API:** Access to the Freelancer API. You will need your API Token and User ID.

---

## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/DVall-c/Freelancer-API-Job-Scraper-Telegram-Notifier.git](https://github.com/DVall-c/Freelancer-API-Job-Scraper-Telegram-Notifier.git)
   cd Freelancer-API-Job-Scraper-Telegram-Notifier

2. **Install requirements.txt:**
   ```bash
   pip install -r requirements.txt

3. **Configure Your Secrets:**
Create a file named settings.py inside the core/ folder (core/settings.py).
Add your credentials in the exact format below. 
DO NOT commit this file to GitHub unless you want strangers hijacking your Telegram bot.
   ```bash
   # core/settings.py
   BOT_TOKEN = "your_telegram_bot_token_here"
   CHAT_ID = "your_personal_chat_id_here"

   # Application Configuration
   FILE_PATH = "jobs.txt"  # Path to your state-of-the-art text file database
   INTERVAL = 30           # Polling interval in seconds

4. **Run main.py**





