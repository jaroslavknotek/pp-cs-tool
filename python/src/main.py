import synchronizer
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--config", help="path to config file", type=str)
args = parser.parse_args()

with open(args.config) as f:
    data = json.load(f)

dir_path = data["dir_path"]
archive_pass = data["archive_pass"]
onedrive_config = data["onedrive"]
synchronizer.sync(dir_path, archive_pass, onedrive_config)
