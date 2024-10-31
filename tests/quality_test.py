import os
from app import prepare

def test_prepare_cols():
    config_path = str(os.environ.get('CONFIG_PATH'))
    df, configs = prepare(config_path)
    assert set(df.columns) == set(configs["output_cols"])