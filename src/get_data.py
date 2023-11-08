
import os
import yaml
import pandas as pd
import argparse

def read_params(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

def get_data(config_path):
    config = read_params(config_path)
    print(config)
    data_path = config["data_source"]["s3_source"]
    df = pd.read_csv(data_path, sep=",", encoding='utf-8')
    print(df.head())
    return df

if __name__ == "__main__":
    script_directory = os.path.dirname(os.path.abspath(__file__))
    default_config_path = os.path.join(script_directory, "params.yaml")

    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default=default_config_path)
    parsed_args = parser.parse_args()
    data = get_data(config_path=parsed_args.config)





