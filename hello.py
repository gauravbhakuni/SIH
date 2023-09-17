import csv

with open('dataset.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        # Access data by column names (keys)
        print(row['Course'], row['Date'], row['Certificate Url'], row['Instructor Name'], row['Name'], row['Course Length'])
