from .client import Client



class Methods(Client):
    # Constants
    GETITEMSELLBUYINFO      = '/Home/GetItemSellBuyInfo'
    GETWORLDMARKETLIST      = '/Home/GetWorldMarketList'
    GETWORLDMARKETSUBLIST   = '/Home/GetWorldMarketSubList'

    def __init__(self, session_id, cookie_token, form_token):
        super().__init__(session_id, cookie_token, form_token)

    def get_item_sell_buy_info(self, item_id):
        self.set_item(item_id)
        data = self.connect(method = self.GETITEMSELLBUYINFO)

        return data

    def get_world_market_sub_list(self, item_id):
        self.set_item(item_id)
        data = self.connect(method = self.GETWORLDMARKETSUBLIST)

        return data

    def get_world_market_list(self, main_category, sub_category):
        """Returns a list of items based on main_category and sub_category

        {
            "marketList": [
                {
                "mainKey"   : ID of the item,
                "sumCount"  : Amount currently posted on the market, 
                "name"      : Name of the item,
                "grade"     : Grade of the item,
                "minPrice"  : Minimum the item can be sold for (not minimum it is listed for)
                },
                ...
            ]
        }
        """
        self.set_main_category(main_category)
        self.set_sub_category(sub_category)
        data = self.connect(method = self.GETWORLDMARKETLIST)

        return data




        

