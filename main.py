from pybithumb import Bithumb
import time
import dotenv
import os
import requests


dotenv.load_dotenv()


bidcnt = 1
svrno = os.getenv("server_no")
mainver = "bt241117001"


for coin in Bithumb.get_tickers()[:15]:
    print(coin, Bithumb.get_current_price(coin))