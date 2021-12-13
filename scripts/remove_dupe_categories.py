import json
from os.path import dirname

categories_file = open(dirname(__file__) + "/../output/categories.json")
categories = json.load(categories_file)

unique_categories = set()
for val in categories:
    unique_categories.add(val["title"])

print(list(unique_categories))

with open(dirname(__file__) + "/../output/categories.json", "w+") as categories_outfile:
    data = {"categories": list(unique_categories)}
    json.dump(data, categories_outfile)
