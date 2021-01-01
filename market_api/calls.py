from .client import Client

import pandas as pd

class Calls(Client):

    def __init__(self, session_id, cookie_token, form_token):
        super().__init__(session_id, cookie_token, form_token)

    def get_market_depth(self, item_id):
        self.set_item(item_id)
        data = self.connect(method = '/Home/GetItemSellBuyInfo')['marketConditionList']

        market_conditions = pd.DataFrame.from_dict(data)

        # Return a DataFrame sorted by given column order.
        return market_conditions[['pricePerOne', 'buyCount', 'sellCount']]
