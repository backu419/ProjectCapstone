from searchfile import searchfile
from threading import Thread

class SearchManager:

    def __init__(self):
        pass
    def search(selfself, filename, drives):
        print("This is a search method manager")

        search_threads = []
        file_searchers = []

        for drive in drives:
            print(drive)
            file_searcher = searchfile()
            file_searcher.task2(drive, filename)

            search_thread = Thread()
            search_thread.start(file_searcher)

            file_searchers.append(file_searcher)
            search_threads.append(search_thread)

        for search_thread in search_threads:
            search_thread.join()

        search_results = []
        for file_searcher in file_searchers:
            search_results.append(file_searcher.task2)