import os
import csv
import json

def main():
    data_path = "vg_filtered.csv"
    data_path2 = "videogame_data.json"
    all_values = {}
    all_values['game'] = []

    with open(data_path, encoding="utf8") as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        first_row = True
        for row in data:
            if first_row:
                first_row = False
            else:
                all_values['game'].append(
                    {
                        'name': row[0],
                        'max_players': int(row[1]),
                        'genre_all': row[2],
                        'genre_one': row[3],
                        'publishers_all': row[4],
                        'publishers_one': row[5],
                        'review_score': int(row[6]),
                        'sales': float(row[7]),
                        'used_price': float(row[8]),
                        'release_console': row[9],
                        'rating': row[10],
                        'release_year': int(row[11]),
                        'length': float(row[12])
                    }
                )

    with open(data_path2, 'w') as jsonfile:
        json.dump(all_values, jsonfile)

if __name__ == '__main__':
        main()