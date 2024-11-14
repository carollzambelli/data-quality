import pandas as pd
import json
from sklearn.pipeline import Pipeline
from src.prepare import Prepare

def test_prepare_cols():
    output_cols = ["id", "preco", "quartos", "banheiros", "area_util", "area_total", "andares", "vista_mar", "qualidade_vista"]
    configs = json.load(open("assets/path_config.json"))
    meta_schema = pd.read_excel(configs["meta_path"], sheet_name="schema")
    df = pd.read_csv(configs["data_path"])
    pp = Prepare(df, meta_schema)

    Pipeline([
        ('seleciona_colunas', pp.select_cols()),
        ('renomeia colunas', pp.rename_cols()),
        ('atribui tipos', pp.data_type()),
        ])

    df = pp.return_data()

    assert set(df.columns) == set(output_cols)