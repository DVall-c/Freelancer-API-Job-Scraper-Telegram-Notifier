import time
import requests
from core.settings import FILE_PATH, INTERVAL 

# define the function for getting projects from Freelancer.com 
# using their API, and we filter them based on how recently they were posted
def get_projects(query="python", limit=5, recent_seconds=60):
    url = "https://www.freelancer.com/api/projects/0.1/projects/active/"
    filters = {
        "query": query,
        "limit": limit,
    }

    try:
        # we make a GET request to Freelancer's API with the specified filters
        response = requests.get(url, params=filters)
        response.raise_for_status() # this will raise an error if the response status code is not 200, which helps us catch issues with the API request
        rawdata = response.json()
    except Exception as e:
        print(f"[API] Error connecting to Freelancer: {e}")
        return []

    print("[API] Listner for a new project...")
    now = time.time() 
    projects = []

    # we check if the API response contains the expected data structure, 
    # and if it does, we iterate through the projects and filter them based on how recently they were posted
    if "result" in rawdata and "projects" in rawdata["result"]:
        for item in rawdata["result"]["projects"]:
            item_title = item["title"]
            raw_item_url = item["seo_url"]
            project_url = f"https://www.freelancer.com/projects/{raw_item_url}/details"
            posted_time = item["time_submitted"]
            
            seconds_ago = int(now - posted_time)
            # if the project was posted within the specified recent_seconds, we add it to our list of projects to return
            if seconds_ago <= recent_seconds:
                # we append the project details to our list of projects, which will be returned to the caller
                projects.append({
                    "title": item_title,
                    "url": project_url,
                    "posted_seconds_ago": seconds_ago
                })

    return projects

def write_job_to_file(project):
    """This function takes a project dictionary and writes its details to the specified file in a structured format,"""
    with open(FILE_PATH, "a", encoding="utf-8") as f:
        f.write(f"Title: {project['title']}\n")
        f.write(f"URL: {project['url']}\n")
        f.write(f"Posted seconds ago: {project['posted_seconds_ago']}\n")
        f.write("----\n")
        f.flush()

def run_scraper():
    """The main loop of the scraper, which continuously checks for new projects and writes them to the file."""
    seen_projects = set()
    print("[Scraper] Searching for new projects...")

    while True:
        try:
            # we call the get_projects function to fetch the latest projects from Freelancer, 
            # and we check if there are any new projects that we haven't seen before (based on their URL)
            projects = get_projects(query="python", limit=20, recent_seconds=60)

            for project in projects:
                if project["url"] not in seen_projects:
                    print(f"[Scraper] We found a project: {project['title']}")
                    write_job_to_file(project)
                    seen_projects.add(project["url"])

            # we wait for the specified interval before checking for new projects again, 
            # to avoid overwhelming the API and to give it time to update with new projects
            time.sleep(INTERVAL)
        except Exception as e:
            print(f"[Scraper] Error... : {e}")
            time.sleep(INTERVAL)