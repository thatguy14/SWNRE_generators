from collections import OrderedDict
import npc_name_generator as name_gen
import parse_rollable_tables as parse_tables
import os
import json

class generate_full_npc(object):

    npc_traits_table = None

    def __init__(self,culture=None,sex=None):

        # Load the data. If a class has already been instatiated, then don't reload.
        self._curr_path = os.path.dirname(os.path.realpath(__file__))
        self._path_name_table = os.path.join(self._curr_path, 'tables/npc_character_tables.json')

        if generate_full_npc.npc_traits_table is None:
            with open(self._path_name_table) as f:
                generate_full_npc.npc_traits_table = json.load(f)
                print('Loaded Json')

        #Create the name generator
        self._name_gen = name_gen.npc_name_generator(culture, sex)

        self._npc_profile = OrderedDict([('Name', None),
                                         ('Culture', None),
                                         ('Sex', None),
                                         ('Age', None)])

        self.rollable_table = parse_tables.parse_rollable_tables()
        self.generate_random_NPC_all(culture,sex)

    def generate_random_NPC_all(self, culture=None, sex=None, reroll_flag=1):
        """iterate over the dictionary to get the different traits

        Traits: Name, Culture, Sex, Age, Background, role in society, Biggest problem, Greatest Desire, Obvious character trait
        """
        self._name_gen.culture = culture
        self._name_gen.sex = sex
        self._name_gen.generate_random_name()

        self._npc_profile["Name"] = self._name_gen.full_name
        self._npc_profile["Culture"] = self._name_gen.culture
        self._npc_profile["Sex"] = self._name_gen.sex

        #Hard code the values - we are sticking with the book and its tables
        self.rollable_table.dict_to_parse = generate_full_npc.npc_traits_table["age"]
        self._npc_profile["Age"] = self.rollable_table.roll_random_from_dic()[0]

        self.rollable_table.dict_to_parse = generate_full_npc.npc_traits_table["Background"]
        self._npc_profile["Background"] = self.rollable_table.roll_random_from_dic()[0]

        self.rollable_table.dict_to_parse = generate_full_npc.npc_traits_table["Society_role"]
        self._npc_profile["Role in Society"] = self.rollable_table.roll_random_from_dic()[0]

        self.rollable_table.dict_to_parse = generate_full_npc.npc_traits_table["biggest_problem"]
        self._npc_profile["Biggest Problem"] = self.rollable_table.roll_random_from_dic()[0]

        self.rollable_table.dict_to_parse = generate_full_npc.npc_traits_table["greatest_desire"]
        self._npc_profile["Greatest Desire"] = self.rollable_table.roll_random_from_dic()[0]

        self.rollable_table.dict_to_parse = generate_full_npc.npc_traits_table["character trait"]
        self._npc_profile["Most Obvious Character Trait"] = self.rollable_table.roll_random_from_dic()[0]

    def __str__(self):
        return_string = ''
        for keys in self._npc_profile:
            return_string = return_string + '\n' + "{}: {}".format(keys, self._npc_profile[keys])
        return return_string


if __name__ == '__main__':
    t = generate_full_npc('Arabic','Female')
    print(t)


