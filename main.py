import threading # for parallel execution of watcher and scraper
from core.listener import watch_and_send
from core.requester import run_scraper

if __name__ == "__main__":
    print("[Sistem] Starting...")

    # start the file watcher in a separate thread so it can run concurrently with the scraper
    watcher_thread = threading.Thread(target=watch_and_send, daemon=True)
    # we set daemon=True so that the watcher thread will automatically close when the main program exits
    watcher_thread.start()
    # now we run the scraper on the main thread, which will keep the program alive and allow the watcher to do its job in the background

    # we wrap the scraper in a try-except block to allow for graceful shutdown on keyboard interrupt (Ctrl+C)
    try:
        run_scraper()
    except KeyboardInterrupt:
        print("\n[Sistem] Mannualy interrupted. Shutting down...")