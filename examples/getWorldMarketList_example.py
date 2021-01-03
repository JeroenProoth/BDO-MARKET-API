import os
import pandas as pd

from secrets import SESSIONID, COOKIETOKEN, FORMTOKEN
from market_api.methods import Methods
from market_api.categories import materials


"""Example showing the use of Methods.get_world_market_list() to get all item IDs,
number of posted items, names, grades and minimum price for items in the materials
section of the marketplace.
"""

methods = Methods(SESSIONID, COOKIETOKEN, FORMTOKEN)

# Create a folder in main folder if it does not already exist.

item_data_path = 'item_data\\materials'

if not os.path.exists(item_data_path):
    os.makedirs(item_data_path)

# materials
category = materials

main_category = category['mainCategory']

for key, sub_category in category['subCategories'].items():

    data = methods.get_world_market_list(main_category, sub_category)['marketList']

    # Pandas orders the headers randomly (sortoff). You can add [[ ]] to order the columns how you want.
    subcategory_data = pd.DataFrame.from_dict(data)[['name', 'mainKey', 'sumCount', 'minPrice', 'grade']]
    subcategory_data.to_csv(item_data_path + '\\' + key + '.csv', sep = "\t", index = False)