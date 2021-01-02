import pandas as pd
import os
from .client import Client



class Calls(Client):
    item_list = pd.read_csv('market_api\\itemsids.csv', sep = ",")
    item_data_path = 'item_data'

    def __init__(self, session_id, cookie_token, form_token):
        super().__init__(session_id, cookie_token, form_token)

        if not os.path.exists(self.item_data_path):
            os.makedirs(self.item_data_path)


    def get_item_id(self, item_name):
        try:
            return self.item_list.loc[self.item_list.Item == str(item_name)].ID.values[0]
        except IndexError:
            raise IndexError("Item with name '{}' not found.".format(item_name))

    def get_item_name(self, item_id):
        try:
            return self.item_list.loc[self.item_list.ID == int(item_id)].Item.values[0]
        except IndexError:
            raise IndexError("Item with ID '{}' not found.".format(item_id))

    def get_item_sell_buy_info(self, item_id):

        self.set_item(item_id)
        data = self.connect(method = '/Home/GetItemSellBuyInfo')

        return data

    def get_market_depth(self, item_id, dump = False):
        """Returns a pandas DataFrame sorted from low -> high.
        Market depth is given by the buy- and sellCounts.
        """

        data = self.get_item_sell_buy_info(item_id)['marketConditionList']

        # Sort DataFrame by given column order.
        market_conditions = pd.DataFrame.from_dict(data)[['pricePerOne', 'buyCount', 'sellCount']]

        if dump:
            item_name = self.get_item_name(item_id).replace(" ", "")
            market_conditions.to_csv(self.item_data_path + '\\' + item_name + '.csv', sep = "\t", index = False)

        return market_conditions

    def get_latest_price(self, item_id, trigger = 'None'):
        """Returns the latest price based on buyCount or sellCount (default).
        If 'buyCount' is used, it returns the highest price someone is willing to pay for it.
        If 'sellCount' is used, it returns the lowest price someone is willing to sell it for.

        If there are no sellorders (as in sellCount == 0 at every pricepoint), return max price.
        """

        market_conditions = self.get_market_depth(item_id)

        if trigger == 'buyCount':
            market_price = market_conditions.loc[market_conditions['buyCount'] != 0].max()['pricePerOne']
            if not pd.isna(market_price):
                return market_price
            return market_conditions['pricePerOne'].max()

        else:
            market_price = market_conditions.loc[market_conditions['sellCount'] != 0].min()['pricePerOne']
            if not pd.isna(market_price):
                return market_price
            return market_conditions['pricePerOne'].max()
