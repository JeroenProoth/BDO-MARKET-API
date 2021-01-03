from .client import Client



class Methods(Client):
    # Constants
    GETITEMSELLBUYINFO      = '/Home/GetItemSellBuyInfo'
    GETWORLDMARKETLIST      = '/Home/GetWorldMarketList'
    GETWORLDMARKETSUBLIST   = '/Home/GetWorldMarketSubList'

    def __init__(self, session_id, cookie_token, form_token):
        super().__init__(session_id, cookie_token, form_token)

    def get_item_sell_buy_info(self, item_id):
        """Returns market information of a given item_id

        {
            "priceList" : [ list of prices item can be sold at],
            "marketConditionList" : [
                {
                "sellCount"     : Amount of items being sold at this pricepoint,
                "buyCounts"     : Amount of items being bought at this pricepoint,
                "pricePerOne"   : Pricepoint
                },
                ...
            ],
            "basePrice"                     : Minimum the item can be sold for (not minimum it is listed for),
            "enchantGroup"                  : No idea,
            "enchantMaterialKey"            : No idea,
            "enchantMaterialPrice"          : No idea,
            "enchantNeedCount"              : No idea,
            "maxRegisterForWorldMarket"     : Maximum amount that can be registered at once,
            "countValue"                    : No idea,
            "sellMaxCount"                  : No idea,
            "buyMaxCount"                   : No idea,
            "resultCode"                    : Resulting code,
            "resultMsg" : '[
                {
                "days"  :  Date,
                "Value" : Value of item at that data
                },
                ...
            ]'
        }

        """
        self.set_item(item_id)
        data = self.connect(method = self.GETITEMSELLBUYINFO)

        return data

    def get_world_market_sub_list(self, item_id):
        """Returns detailList of a given item_id
        
        {
            "detailList" : [
                {
                "pricePerOne"       : Price of one item,
                "totalTradeCount"   : Total amount of items traded up till now,
                "keyType"           : No idea,
                "mainKey"           : ID of the item,
                "subKey"            : No idea,
                "count"             : Stock of the item,
                "name"              : Name of the item,
                "grade"             : Grade of the item,
                "mainCategory"      : Main category item belongs to,
                "subCategory"       : Sub category item belongs to,
                "chooseKey"         : No idea,                
                }
            ],
            "resultCode"     : Resulting code,
            "resultMsg"      : Resulting message
        }

        """
        self.set_item(item_id)
        data = self.connect(method = self.GETWORLDMARKETSUBLIST)

        return data

    def get_world_market_list(self, main_category, sub_category):
        """Returns a list of items based on main_category and sub_category

        {
            "marketList" : [
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




        

