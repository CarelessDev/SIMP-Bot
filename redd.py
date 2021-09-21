from libraryimport import *

from dotenv import load_dotenv
import os

load_dotenv()

reddit = asyncpraw.Reddit(client_id=os.getenv("client_id"),
                          client_secret=os.getenv("client_secret"),
                          username=os.getenv("username"),
                          password=os.getenv("password"),
                          user_agent=os.getenv("user_agent"))
