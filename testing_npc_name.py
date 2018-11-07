# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 14:54:41 2018

@author: Matthew
"""

import npc_name_generator as nng
r = nng.npc_name_generator()
t = nng.parse_rollable_tables()
t.dict_to_parse = r.full_name_tables
t.create_grouped_dictionary()

#tt = nng.npc_name_generator()

#test_key = '99-100'
#test_key2 = '100'

