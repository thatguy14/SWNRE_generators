# -*- coding: utf-8 -*-
"""
Module to generate NPC names according to the Stars Without Number Revised Edition (SWNRE).

This module will can generate the name culture and sex of an npc. It will handle its own file loading.
Classes:
    npc_name_generator: NPC Name Generator based on random or specified culture and sex
    prase_rollable_tables: Helper class that can parse the tables as outputted from the SWNRE

Created on Fri Nov  2 13:27:02 2018

@author: Matthew
"""
import random as rnd
from collections import OrderedDict
import json
import os
import random
import parse_rollable_tables

class npc_name_generator(object):
    """ Generate the name, sex, and culture of an NPC

    Keyword Arguments:
        :param culture -- Specified culture to use. Must correspond to the available list (default random (None))
        :param sex -- Specified Sex, male or female (default random (None))
    """

    full_name_tables = None
    num_table_cultures = None
    
    def __init__(self, culture_input=None, sex_input=None):
        """Initialize the parse_rollable_tables class, randomize culture and sex if necessary (no input), generate a name

        :param culture: default random, specified culture of NPC
        :param sex: default
        """

        # Begin by loading the name table
        self._curr_path = os.path.dirname(os.path.realpath(__file__))
        self._path_name_table = os.path.join(self._curr_path, 'tables/Name_tables_all.json')
        
        # Check to see if another npc_name has been loaded and if not, load the data
        if npc_name_generator.full_name_tables is None:
            with open(self._path_name_table) as f:
                npc_name_generator.full_name_tables = json.load(f)
                print('Loaded Json')
                
        if npc_name_generator.num_table_cultures is None:
            npc_name_generator.num_table_cultures = len(npc_name_generator.full_name_tables.keys())
        
        self._culture = None
        self._sex = None
        # Set culture and sex, random if the user didn't pass it in
        self.culture = culture_input
        self.sex = sex_input

        # Initialize the rollable table
        self.rollable_table = parse_rollable_tables.parse_rollable_tables()
        

            
        self.generate_random_name()
            
    @property
    def culture(self):
        return self._culture

    @culture.setter
    def culture(self, culture):
        if culture is None:
            self._culture = self.generate_random_culture()
        else:
            culture_list = self.return_culture_list()
            if culture in culture_list:
                self._culture = culture
            else:
                raise Exception('Culture not found in culture list')
    @property
    def sex(self):
        if self._sex == 0:
            return "Male"
        elif self._sex == 1:
            return "Female"

    @sex.setter
    def sex(self, sex_value):
        #Set Sex value
        if sex_value is None:
            self.generate_random_sex()
        elif not (sex_value == 0 or sex_value == 1 or sex_value == "Male" or sex_value == "Female"):
            raise Exception("Sex value is incorrect")
        elif sex_value == "Male":
            self._sex = 0
        elif sex_value == "Female":
            self._sex = 1
        else:
            self._sex = sex_value

    def generate_random_culture(self):
        # Generates a random culture based on the loaded list

        rand_cult_num = random.randint(0, npc_name_generator.num_table_cultures-1)
        culture_keys = list(npc_name_generator.full_name_tables.keys())
        return culture_keys[rand_cult_num]
    
    def generate_random_sex(self):
        # Generated a random sex, 0 means male, 1 means female

        rand_sex_num = random.randint(0, 1)  # 0 is male, 1 is female
        
        if rand_sex_num == 0:
            self.sex = 0
        elif rand_sex_num == 1:
            self.sex = 1
            
    def generate_random_name(self):
        # Generates a random name once sex and culture have been set


        curr_name_dict = npc_name_generator.full_name_tables[self.culture]
        self.rollable_table.dict_to_parse = curr_name_dict        
        
        rand_firstname_num = random.randint(1,self.rollable_table.largest_dice_roll)
        rand_lastname_num = random.randint(1,self.rollable_table.largest_dice_roll)
        
        firstname_group_list = self.rollable_table.get_dic_group(rand_firstname_num)
        lastname_group_list = self.rollable_table.get_dic_group(rand_lastname_num)
        
        self.firstname = firstname_group_list[self._sex]
        self.lastname = lastname_group_list[2]
        self.full_name = '{} {}'.format(self.firstname, self.lastname)

    @staticmethod
    def return_culture_list():
        return list(npc_name_generator.full_name_tables.keys())
        
    def __str__(self):
        return 'Name: {}, Sex: {}, Culture: {}'.format(self.full_name, self.sex, self.culture)

    def get_npc_list(self):
        return [self.full_name, self.sex, self.culture]

if __name__ == '__main__':
    r = npc_name_generator('Arabic')
    print(r)
