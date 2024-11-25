from pybithumb import Bithumb
import time
import dotenv
import os
import requests

dotenv.load_dotenv()

bidcnt = 1
svrno = os.getenv("server_no")
mainver = "bt241117001"
conkey = os.getenv("key1")
seckey = os.getenv("key2")


bithumb = Bithumb(conkey, seckey)
for coin in Bithumb.get_tickers():
    print(coin, bithumb.get_balance(coin))