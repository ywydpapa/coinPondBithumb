from pybithumb import Bithumb
import time
import dotenv
import os
import requests

dotenv.load_dotenv()

bidcnt = 1
svrno = os.getenv("server_no")
mainver = "bt241117001"
conkey = os.getenv("key3")
seckey = os.getenv("key4")


bithumb = Bithumb(conkey, seckey)
print(bithumb.get_balance("BTC"))
