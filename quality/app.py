"""
Main module to prepare data and generate validation logs
"""
import sys
import pandas as pd
import json
from sklearn.pipeline import Pipeline
from prepare import Prepare
from validator import Validator
import logging

def prepare(config_path):

    configs = json.load(open(config_path))
    meta_schema = pd.read_excel(configs["meta_path"], sheet_name="schema")
    df = pd.read_csv(configs["data_path"])
    pp = Prepare(df, meta_schema)

    Pipeline([
        ('seleciona_colunas', pp.select_cols()),
        ('renomeia colunas', pp.rename_cols()),
        ('atribui tipos', pp.data_type()),
        ])

    return pp.return_data(), configs


def generate_report(config_path):

    df, configs = prepare(config_path)

    logging.basicConfig(filename=configs["report_path"], level=logging.INFO)
    meta_quality = pd.read_excel(configs["meta_path"], sheet_name="quality")
    val = Validator(df, meta_quality)

    for f in configs["funcs_validation"]:
        func = getattr(val, f)
        func()

    return True


if __name__ == '__main__':
    generate_report(sys.argv[1])