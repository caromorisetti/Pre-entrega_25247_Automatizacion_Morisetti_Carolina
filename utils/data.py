import csv
import pathlib
# Lee el csv y lo guarda en una lista de tuplas
def csv_login(file_path):
    path = pathlib.Path(file_path)
    data = []
    with path.open(newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            should_work = row['should_work'].lower() == 'true'            
            data.append((row['user'], row['password'], should_work))
    return data
