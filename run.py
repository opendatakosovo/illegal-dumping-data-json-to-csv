import requests
import json
import csv

r = requests.get('http://opendatakosovo.org/app/illegal-dumps/static/data/dumps.js')

if r.status_code == 200:
    dump_sites_str = r.text.replace('var dumps = ', '')
    dump_sites = json.loads(dump_sites_str)

    with open('illegal-dumps.csv', 'w') as csv_file:
        wr = csv.writer(csv_file, delimiter=',')

        # Header
        wr.writerow(["Latitude", "Longitude", "Size", "Type", "Image URL"])

        # Data
        for dump_site in dump_sites:
            csv_row = [
                dump_site["location"]["lat"],
                dump_site["location"]["lon"],
                dump_site["size"],
                ",".join(dump_site["type"]),
                dump_site["imgUrl"]
            ]

            wr.writerow(csv_row)
            print str(csv_row)
else:
    print 'Request for data failed. Check URL.'
