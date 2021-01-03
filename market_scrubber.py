import time
import pandas as pd
from market_api.methods import Methods
from masteries.cooking import CookingMastery

class MarketScrubber():

    def __init__(self, session_id, cookie_token, form_token, item_dataframe):
        self.methods = Methods(session_id, cookie_token, form_token)
        self.item_dataframe = item_dataframe

    def get_item_id(self, item_name):
        return self.item_dataframe.loc[(self.item_dataframe.name).apply(lambda x : x.casefold()) == str(item_name).casefold()].mainKey.values[0]

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

    def get_item_price(self, item):
        """Returns the price of an item.
        """
        if not item.isdigit():
            item = self.get_item_id(item)

        data = self.methods.get_world_market_sub_list(item)['detailList']
        item_value = data[0]['pricePerOne']

        return item_value

    def calculate_recipe_profitability(self, recipe, mastery):
        """Returns the input and output value of a recipe based on mastery level.
        Used formulas provided by https://docs.google.com/spreadsheets/d/1D7mFcXYFm4BUS_MKxTvgBY2lXkGtwWqn2AW91ntUvzE/edit#gid=1519713712

        returns a tuple (input value, output value)
        """
        cm = CookingMastery(mastery)

        max_proc_chance = cm.regular_rare_max_chance()
        rare_proc_chance = cm.rare_proc_chance()

        outputs = recipe['output']
        inputs = recipe['input']

        input_value = 0
        output_value = 0

        for item, amount in inputs.items():
            input_value += float(amount) * self.get_item_price(item)

        for item, rarity in outputs.items():
            if rarity == 'normal':
                items_created = 2.5 + 1.5 * max_proc_chance
                output_value += items_created * self.get_item_price(item)

            else:
                items_created = (1.5 + 0.5 * max_proc_chance) * (0.2 + rare_proc_chance)
                output_value += items_created * self.get_item_price(item)

        return (input_value, output_value)

