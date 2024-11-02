"""
Data validation module. 
"""
import  numpy as np
import logging
import pandas as pd
import datetime
    
logger = logging.getLogger()

class Validator:
    
    def __init__(self, data, _config):
        self.data = data
        self.configs = _config
        self.i_limits = self.configs.loc[self.configs['limits_validation'] == 1].index
        self.keys = list(self.configs.loc[self.configs['key_validation'] == 1]["variavel"])
        self.i_null = self.configs.loc[self.configs['null_validation'] == 1].index
        self.i_dist = self.configs.loc[self.configs['distribution_validation'] == 1].index

    def key_validation(self):
        if self.data[self.keys].nunique().item() != len(self.data):
            logger.warning(
                f"KEY_DUPLICATION ; {self.keys}; {datetime.datetime.now()}")

    def null_validation(self):
        for i in self.i_null:
            value = self.configs.iloc[i]["value"]
            col = self.configs.iloc[i]["variavel"]
            value_dev = self.configs.iloc[i]["value_dev"]
            n_null = len(self.data.loc[self.data[col].isnull()])/len(self.data)
            if not value - value_dev <= n_null <= value + value_dev:
                logger.warning(
                    f"NULL_TOLERANCE ; {col}; {datetime.datetime.now()}")

    def distribution_validation(self):
        for i in self.i_dist:
            value = self.configs.iloc[i]["value"]
            col = self.configs.iloc[i]["variavel"]
            categ = self.configs.iloc[i]["category"]
            value_dev = self.configs.iloc[i]["value_dev"]
            if not value - value_dev <= len(self.data[self.data[col] == categ]) <= value + value_dev:
                logger.warning(
                    f"DISTRIBUTION_DEVIATION ; {col}; {datetime.datetime.now()}")
                
    def limits_validation(self):
        for i in self.i_limits:
            value = self.configs.iloc[i]["value"]
            operator = self.configs.iloc[i]["operator"]
            col = self.configs.iloc[i]["variavel"]
            execution = f"self.data.loc[self.data.{col} {operator} {value}]"
            n =len(eval(execution))
            if n > 0:
                logger.warning(
                    f"{n} CASES OUT OF BOUNDS ; {col}; {datetime.datetime.now()}")
