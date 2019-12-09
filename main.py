import pandas as pd

CSV_LOCATION = "your_csvfile.csv"
FULL_JSON_LOCATION =  "location_json_file.json"
DROP_JSON_LOCATION =  "location_json_file_droped.json"
COLUMN_TO_DROP = "colunm_name"

csv_file = CSV_LOCATION
data = pd.read_csv(csv_file)
json_file = FULL_JSON_LOCATION
data.to_json(json_file, orient="records")

new_data = data.drop(COLUMN_TO_DROP , axis=1)

json_file_droped = DROP_JSON_LOCATION
new_data.to_json(json_file_droped, orient="records")