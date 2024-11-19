import os
import pyupbit
import time
from datetime import datetime
import pymysql
import random
import pandas as pd
import dotenv


dotenv.load_dotenv()
hostenv = os.getenv("host")
userenv = os.getenv("user")
passwordenv = os.getenv("password")
dbenv = os.getenv("db")
charsetenv = os.getenv("charset")


db = pymysql.connect(host=hostenv, user=userenv, password=passwordenv, db=dbenv, charset=charsetenv)
serverNo = 2
serviceNo = 240808