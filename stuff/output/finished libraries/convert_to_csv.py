import json
import os
import csv

userInput = input("Please enter name of json directory (e.g. matplotlib) to convert to a csv file: \n")

for file in os.listdir(f'{userInput}'):
    if file.endswith(".json"):
        
        with open(f'{userInput}/{file}') as json_file:
            data = json.load(json_file)
            print(data)

        py_function = open('output.csv', 'a')
        csvwriter = csv.writer(py_function)
        # csvwriter.writerow(data.keys())
        csvwriter.writerow(data.values())


py_function.close()

