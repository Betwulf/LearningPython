import pandas as pd

json_file = 'data.json'
with open(json_file, 'rt', encoding='utf-8') as f:
    json_data = pd.read_json(f)
    print(json_data)
