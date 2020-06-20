import multiprocessing
import os

workers = int(os.getenv("GUNICORN_WORKERS_COUNT", multiprocessing.cpu_count() * 4))
timeout = 3
