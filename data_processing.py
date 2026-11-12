import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []

def filter_items(condition, dict_list):
    result = filter(condition, dict_list)
    return list(result)

def aggregate(aggregation_key, aggregation_function, dict_list):
    values = list(map(lambda item: float(item[aggregation_key]), dict_list))
    return aggregation_function(values)

with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
print(aggregate("temperature", lambda x: sum(x) / len(x), cities))
print()

# Print all cities in Germany
print("The City in Germany is")
germany = filter_items(lambda x: x['country'] == "Germany", cities)
print(germany)
print()

# Print all cities in Spain with a temperature above 12°C
print("all cities in Spain with a temperature above 12°C")
spain_temp = filter_items(lambda x: x['country'] == "Spain" and float(x['temperature']) > 12, cities)
print(spain_temp)
print()

# Count the number of unique countries
print("unique countries")
print(len(set(map(lambda x: x["country"], cities))))
print()

# Print the average temperature for all the cities in Germany
print("average temperature for all the cities in Germany")
print(aggregate("temperature",lambda x: sum(x) / len(x),filter_items(lambda x: x["country"] == "Germany", cities)))
print()

# Print the max temperature for all the cities in Italy
print("max temperature for all the cities in Italy")
print(aggregate("temperature",max,filter_items(lambda x: x["country"] == "Italy", cities)))

