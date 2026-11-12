import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

# Print first 5 cities only
for city in cities[:5]:
    print(city)

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = []  
for city in cities:
    temps.append(float(city['temperature']))
print(sum(temps)/len(temps))
print()

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = [float(city['temperature']) for city in cities]
print(sum(temps)/len(temps))
print()

# Print all cities in Germany

print("The City in Germany is")
Germany = []
for city in cities:
    if city["country"] == "Germany":
        Germany.append(city['city'])
print(Germany)

# Print all cities in Spain with a temperature above 12°C

print("all cities in Spain with a temperature above 12°C")
out = []
for city in cities:
    if city['country'] == "Spain" and float(city['temperature']) > 12:
        out.append(city['city'])
print(out)

# Count the number of unique countries
print("unique countries")
unique = []
for city in cities:
    unique.append(city['country'])
news = set(unique)
print(news)

# Print the average temperature for all the cities in Germany
print("average temperature for all the cities in Germany")
germany_temp = []
for city in cities:
    if city['country'] == "Germany":
        germany_temp.append(float(city['temperature']))
new_list = (lambda x: sum(x) / len(x))
print(new_list(germany_temp))

# Print the max temperature for all the cities in Italy
print("max temperature for all the cities in Italy")
italy_temp = []
for city in cities:
    if city['country'] == "Italy":
        italy_temp.append(float(city['temperature']))
print(max(italy_temp))

