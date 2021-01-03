# Used table provided by https://incendar.com/bdo_cooking_mastery_table.php
import math

class CookingMastery():
    def __init__(self, mastery_level):
        self.mastery_level = mastery_level

    def change_mastery_level(self, mastery_level):
        self.mastery_level = mastery_level

    def regular_rare_max_chance(self):
        """Returns an APPROXIMATION of proccing the max amount of crafts.
        """
        chance = (1.28981e-7 * pow(self.mastery_level, 2) + 
            4.6143611e-5 * self.mastery_level + 0.003083753343)

        if chance < 1:
            return chance
        return 1

    def rare_proc_chance(self):
        """Returns an APPROXIMATION of proccing a rare item when crafting.
        """
        chance = (3.9741e-8 * pow(self.mastery_level, 2) + 
            1.6630095e-5 * self.mastery_level +0.001280933474)

        if chance < 1:
            return chance
        return 1

    def mass_produce_chance(self):
        """Returns an APPROXIMATION of proccing a mass production when crafting.
        It has a slightly bigger error, however it only affects crafting time.
        """
        chance = (0.111549286428 * math.exp(self.mastery_level * 0.001115449335))

        if chance < 1:
            return chance
        return 1

    def imperial_bonus(self):
        if self.mastery_level < 1200:
            chance = (5.11622e-7 * pow(self.mastery_level, 2) +
                1.5397922e-4 * self.mastery_level + 0.006933470085)
        else:
            chance = (0.000654905882  * self.mastery_level + 0.13192794117)

        return chance