import time
import pandas as pd
from market_api.methods import Methods

class MarketScrubber():

    def __init__(self, session_id, cookie_token, form_token, item_dataframe):
        self.methods = Methods(session_id, cookie_token, form_token)
        self.item_dataframe = item_dataframe

    def get_item_id(self, item_name):
        return self.item_dataframe.loc[self.item_dataframe.name == str(item_name).title()].mainKey.values[0]

    def get_item_name(self, item_id):
        return self.item_dataframe.loc[self.item_dataframe.mainKey == int(item_id)].name.values[0]

    def get_market_depth(self, item):
        """Returns a pandas DataFrame sorted from low -> high.
        Market depth is given by the buy- and sellCounts.

        returns a DataFrame
        """
        if not item.isdigit():
            item = self.get_item_id(item)

        data = self.methods.get_item_sell_buy_info(item)['marketConditionList']
        market_conditions = pd.DataFrame.from_dict(data)[['pricePerOne', 'buyCount', 'sellCount']]

        return market_conditions

    def get_items_sold(self, item, time_format = 'unix'):
        """Returns the total amount of items sold for a given item.

        returns a tuple with (time_data (unix or local), total items sold)

        time_format: 'unix' (default) or 'local'.
        """
        if not item.isdigit():
            item = self.get_item_id(item)

        time_data = time.time()
        if time_format == 'local':
            time_data = time.strftime("%d:%m:%y %H:%M:%S", time.localtime(time_data))


        data = self.methods.get_world_market_sub_list(item)['detailList']
        items_sold = data[0]['totalTradeCount']

        return (time_data, items_sold)

    def calculate_recipe_cost(self, recipe):
        pass