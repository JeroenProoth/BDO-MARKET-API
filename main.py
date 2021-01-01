"""

Thank you
https://curl.trillworks.com/
https://github.com/Ruwann

"""
import requests, json
import pandas as pd

from secrets import SESSIONID, COOKIETOKEN, FORMTOKEN
from market_api.calls import Calls

client = Calls(SESSIONID, COOKIETOKEN, FORMTOKEN)
client.get_market_depth('9609')

# print(json.dumps(client.connect(), indent = 1))