# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 13:44:02 2018

@author: Matthew
"""

from collections import OrderedDict
import os
import glob
import csv
import json

"""
This module will allow the user to convert csv tables into JSON files for importing. The structure will be:
    
    Culture Dict - 
        Culture : Dice table (dict) 
    
    and
    
    Dice_table (dict)-
    
        DiceRoll : [FirstName_Male FirstName_Female Surname]
        
    Assumes we are in the directory with the CSV files
    
    To use:
        Place this file in the directory containing the csv files and run.
"""

curr_path = os.path.dirname(os.path.realpath(__file__))

csv_files = glob.glob(curr_path + '/*.csv')
full_table_culture = OrderedDict()


for i in range(len(csv_files)):
    curr_culture_name = os.path.split(csv_files[i])[1].replace('.csv','') #Get the current culture name
    dice_tables_names = OrderedDict()
    #read the CSV
    with open(csv_files[i],'r') as csvfile:
        table_reader = csv.reader(csvfile)
        for row in table_reader:
            dice_tables_names[row[0]] = row[1:]
    full_table_culture[curr_culture_name] = dice_tables_names

#We have a dictionary as specified above, now we need to generate the json file and export it
with open('Name_tables_all.json','w') as fp:
    json.dump(full_table_culture,fp)