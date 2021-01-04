import requests

import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WebScraper():
    def __init__(self, item_dataframe):
        self.item_dataframe = item_dataframe


    def get_item_id(self, item_name):
        """Returns item_id given an item_id."""
        return self.item_dataframe.loc[(self.item_dataframe.name).apply(lambda x : x.casefold()) == str(item_name).casefold()].mainKey.values[0]

    def get_item_name(self, item_id):
        """Returns item_name given an item_id."""
        return self.item_dataframe.loc[self.item_dataframe.mainKey == int(item_id)].name.values[0]

    def get_recipe(self, item):
        if not item.isdigit():
            item = self.get_item_id(item)

        URL = 'https://bdocodex.com/us/item/{}/'.format(item)
        page = requests.get(URL)
        driver = webdriver.Chrome()

        driver.get(URL)
        
        # WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "dt-reward")))

        

        materials = []
        total_time = 0

        recipe = {self.get_item_name(item) : {'output' : {}, 'input' : {}}}

        """ Sometimes it doesn't work, so I did this.
        This work quite consistently within 2 seconds, so don't change it.

        I tried all kinds of shit with WebDriverWait, I couldn't make it work.
        """
        while not materials:
            page = BeautifulSoup(driver.page_source, 'lxml')
            product = page.find(id='tabs-productofrecipe')
            materials = product.find_all("td", {"class": "dt-reward"}, limit = 2)

            time.sleep(1)
            total_time +=1

            if total_time > 60:
                break


        inputs = materials[0]
        outputs = materials[1]

        lines = inputs.find_all("a", class_ = 'qtooltip')
        for line in lines:
            amount = line.find("div", class_='quantity_small nowrap')
            for attr in str(line).split(" "):
                if 'data-id' in attr:
                    item_id = attr.replace('data-id=', '').replace('item--', '').replace('"', '').replace('--', ' ')
            if  amount != None:
                amount = int(amount.text)
            else:
                amount = 1
            recipe[self.get_item_name(item)]['input'][item_id] = amount

        lines = outputs.find_all("a", class_ = 'qtooltip')
        for line in lines:
            amount = line.find("div", class_='quantity_small nowrap')
            for attr in str(line).split(" "):
                if 'data-id' in attr:
                    item_id = attr.replace('data-id=', '').replace('item--', '').replace('"', '').replace('--', ' ')
            if  amount != None:
                amount = int(amount.text)
            else:
                amount = 1

            if len(recipe[self.get_item_name(item)]['output']) < 1: 
                recipe[self.get_item_name(item)]['output'][item_id] = 'normal'
            else:
                recipe[self.get_item_name(item)]['output'][item_id] = 'rare'

        return recipe

    def get_material_group(self, material_group):
        """There are a total of 56 material groups"""

        try:
            group = material_group.split(" ")[1]

            group = {material_group : {} }
            page = requests.get('https://bdocodex.com/us/materialgroup/{}/'.format(group))
            soup = BeautifulSoup(page.content, 'html.parser')

            insider = soup.find("div", class_='insider')
            for line in insider:
                for attr in str(line).split(" "):
                    if 'data-id' in attr:
                        item_id = attr.replace('data-id=', '').replace('item--', '').replace('"', '').replace('--', ' ')
                        group[material_group][self.get_item_name(item_id)] = item_id

            return group

        except (IndexError, TypeError):
            return None
