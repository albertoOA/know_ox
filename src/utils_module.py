#!/usr/bin/env python3
# coding=utf-8
# Author: Alberto Olivares Alarcos <aolivares@iri.upc.edu>, Institut de Robòtica i Informàtica Industrial, CSIC-UPC


import os
import pandas as pd
from pathlib import Path
from collections import Counter, defaultdict

class utilsModule:
    def __init__(self):
        aux_ = os.path.abspath(__file__)
        self.repository_name = "know_rox"
        self.main_path = aux_[:aux_.find(self.repository_name)+len(self.repository_name)] # find starting pose and add upto that pose + length
        self.csv_file_path = self.main_path + "/csv"

    def create_dict_from_csv_file(self, csv_file_path, csv_file_name, separator):
        """
        Creates a dictionary from the data stored in a csv file.

        Args:
            csv_file_path: a path to a csv file (without the last '/', it is added here)
            csv_file_name: a csv file name (including the .csv)
            separator: the separator used in the file

        Returns:
            A dictionary with the first row of the csv file as keys and the rest of the values 
            as a list (for each key).
        """

        out_dict = dict()

        data = pd.read_csv(csv_file_path + "/" + csv_file_name, sep=separator) #data frame
        out_dict = data.to_dict(orient='list') # dict of lists (first row as 'k')
        #print(out_dict)
        
        return out_dict
    
    def create_csv_file_from_dict(self, dict_in, csv_file_path, csv_file_name):
        """
        Creates a dictionary from the data stored in a csv file.

        Args:
            dict_in: a dictionary to be stored as CSV file
            csv_file_path: a path to a csv file (without the last '/', it is added here)
            csv_file_name: a csv file name (including the .csv)

        Returns:
            None.
        """

        out_dict = dict()

        df = pd.DataFrame.from_dict(dict_in, orient='columns')
        df.to_csv(csv_file_path + '/' + csv_file_name, index=False) # data frame    
