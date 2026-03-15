# file_watcher.py
import time
import os
from core.messager import send_telegram_message
from core.settings import FILE_PATH

def watch_and_send():
    """watching for any new job entries in the file and sending them to Telegram."""
    print(f"[Watcher] Watching {FILE_PATH} from the background...")
    # if the file doesn't exist, create it (this is important for the first run)
    if not os.path.exists(FILE_PATH):
        open(FILE_PATH, 'w', encoding='utf-8').close()
    # we open the file in read mode and keep it open to watch for new lines being added by the scraper
    with open(FILE_PATH, 'r', encoding='utf-8') as f:
        # read only the new lines added to the file if the file already has content
        f.seek(0, os.SEEK_END)
        job_buffer = ""
        
        while True:
            # we read the file line by line, and we use a buffer to accumulate lines 
            # until we hit the separator "----\n" which indicates the end of a job entry
            line = f.readline()
            if not line:
                time.sleep(0.5)
                continue
            
            job_buffer += line
            
            # file separator for jobs is "----\n", so we check for it to know when to send the message
            if "----" in line: # this means we have a complete job entry to send
                clean_msg = job_buffer.replace("----\n", "").strip() # we clean the message by removing the separator and any extra whitespace
                if clean_msg: # we only send if there's actually something to send (in case of empty entries)
                    send_telegram_message(clean_msg) # we send the accumulated job entry to Telegram
                # we reset the buffer for the next job entry
                job_buffer = "" # temporary storage for the job details until we have a complete job entry to send 