from collections import OrderedDict

class parse_rollable_tables(object):
    """ Parse table exported from the SWNRE, particularly ones with multiple dice rolls associated with multiple outcomes

    This class expects a dictionary with the keys being the dice rolls and the entry being the associated outcome.
    If the outcome has multiple entries (i.e., a list) it will return all entries

    :param dict_in: The dictionary that needs to be parsed.

    :return The "thing" associated with that particularly dice roll. May be different types based on what was passed in as the dictionary

    """

    def __init__(self, dict_in=None):
        self._dict_to_parse = dict_in
        if self._dict_to_parse is not None:
            self.create_grouped_dictionary()
            self.set_dice_extent()

    @property
    def dict_to_parse(self):
        return self._dict_to_parse

    @dict_to_parse.setter
    def dict_to_parse(self, dict_in):
        self._dict_to_parse = dict_in
        self.create_grouped_dictionary()
        self.set_dice_extent()

    def create_grouped_dictionary(self):
        # This assumes the dice roller is in the format x-y or just a single number
        # Creates a dictionary of the format dice_value : group where group indicates the key number in the original list that we should use
        dict_dice_keys = list(self._dict_to_parse.keys())

        dice_roll_mapped_dic = OrderedDict()

        counter = 0

        for key in dict_dice_keys:
            dice_range = key.split('-')

            if len(dice_range) == 1:
                nums = list(map(int, dice_range[0]))[0]
                dice_roll_mapped_dic[nums] = counter
                counter += 1
            elif len(dice_range) == 2:
                nums = list(map(int, dice_range))
                first_num = nums[0]
                last_num = nums[1]
                dice_range_list = range(first_num, last_num + 1)
                for dice_num in dice_range_list:
                    dice_roll_mapped_dic[dice_num] = counter
                counter += 1
            else:
                # The data is not in the correct format
                return None
        self.mapped_dice_range = dice_roll_mapped_dic

    def set_dice_extent(self):
        self.largest_dice_roll = list(self.mapped_dice_range.keys())[-1]

    def get_dic_group(self, random_number):
        self.create_grouped_dictionary()
        group_num = self.mapped_dice_range[random_number]
        keys_dict = list(self._dict_to_parse.keys())
        return self._dict_to_parse[keys_dict[group_num]]