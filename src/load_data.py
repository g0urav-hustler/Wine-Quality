# read data from data source 
# save it in data/raw for further process

import os, argparse
from get_data import read_params, get_data


def load_and_save(config_path):
    config = read_params(config_path=config_path)
    df = get_data(config_path=config_path)

    # clear the gaps of coulumn name
    new_col = [col.replace(" ", "_") for col in df.columns]
    raw_data_path = config["load_data"]["raw_dataset_csv"] # save data path 
    df.to_csv(raw_data_path, sep = ",", index= False, header= new_col) # save the data frame



if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default = "params.yaml")
    parsed_args = args.parse_args()
    load_and_save(parsed_args.config) # save the data to raw