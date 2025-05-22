# File: query_table.py

import os
import logging
import yaml

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)

DATA_FILE = '/data/data.yaml'
OUTPUT_FILE = '/data/result.txt'

with open("/data/data.yaml", 'r') as file:
  data = yaml.load(file, Loader=yaml.FullLoader)

data[0]['test'] = 'MTG'

with open('/data/result.txt', 'w') as file:
  file.write(yaml.dump(data, default_flow_style=None, width=70))