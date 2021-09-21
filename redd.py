from libraryimport import *
<<<<<<< HEAD
reddit = asyncpraw.Reddit(client_id = "spAS-xBqUiRD8SV8A6D1Gg", 
                    client_secret="vJJzxCPen2sjXAdX_kTPZxMMCnf5hQ",
                    username="Informal-Ad-2398",
                    password="Qwentyrufuwojd1",
                    user_agent="kawaiipraw")
=======
import os
from dotenv import load_dotenv

load_dotenv()

reddit = asyncpraw.Reddit(client_id=os.getenv("client_id"),
                          client_secret=os.getenv("client_secret"),
                          username=os.getenv("username"),
                          password=os.getenv("password"),
                          user_agent=os.getenv("user_agent"))
>>>>>>> 6eecb8702737799b9e26cb37d4b9ab10208d84e8
