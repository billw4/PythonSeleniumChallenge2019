import threading
from queue import Queue
from advanced_challenges.webcrawler.spider import Spider
from advanced_challenges.webcrawler.domain import *
from advanced_challenges.webcrawler.general import *

# PROJECT_NAME = 'mwaw'
# HOMEPAGE = 'https://marvelousworkandawonder.com/'
PROJECT_NAME = 'copart'
HOMEPAGE = 'https://www.copart.com/'

DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 8
queue = Queue()
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)


# Create worker threads (will die when main exits)
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


# Do the next job in the queue
def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()


# Each queued link is a new job
def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()


# Check if there are items to crawl in queue
def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + ' links left to crawl.')
        create_jobs()


create_workers()
crawl()
