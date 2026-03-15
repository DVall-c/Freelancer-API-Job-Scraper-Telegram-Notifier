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

2. Create and activate a virtual environment (highly recommended):

# On Windows:
.\venv\Scripts\activate
# On macOS and Linux:
source venv/bin/activate

Install the required dependencies:
pip install -r requirements.txt


3. Configure your secrets:

Create a file named settings.py in the core/ folder (core/settings.py).
Add your credentials in this format (DO NOT share this file!):

Python
# core/settings.py
BOT_TOKEN = "your_telegram_bot_token_here"
CHAT_ID = "your_personal_chat_id_here"

# Application Configuration
FILE_PATH = "jobs.txt"  # Path to your log file
INTERVAL = 30  # Polling interval in seconds
🚀 Usage
Simply run the main orchestrator script:

Bash
python main.py
You should see logs in your terminal confirming that the application is hunting for jobs. Notifications will start arriving on your Telegram as new projects are posted.

🧪 For Developers: How to Test Manually
This is a key feature to speed up development without waiting for real jobs to be posted:

Start the application: python main.py.

Open your local jobs.txt file in any text editor.

Paste the following formatted job block at the bottom of the file:

Plaintext
Title: Senior Python Django Engineer
URL: [https://www.freelancer.com/projects/python/details/](https://www.freelancer.com/projects/python/details/)
Posted seconds ago: 42
----
Save the file (Ctrl+S).

Check your Telegram. Your bot should have just sent you a notification for the job you just pasted.

🗺️ Roadmap & Upcoming Features
This project is a work in progress! Here's what's planned for future releases:

[ ] Interactive Telegram Control: Manage the scraper directly from Telegram (start/stop, change keywords).

[ ] Dynamic Bid Templates: Select and send highly personalized bid templates for each job, controlled via Telegram inline keyboards.

[ ] Advanced Filtering: Add logic to filter jobs by budget, client rating, or project type (e.g., fixed-price vs. hourly).

📄 License & Disclaimer
This project is licensed under the MIT License - see the LICENSE file for details.

Disclaimer: Spamming the Freelancer API with excessive requests may result in your IP being banned. Use a reasonable polling interval. The author is not responsible for any actions taken by Freelancer.com against your account.
