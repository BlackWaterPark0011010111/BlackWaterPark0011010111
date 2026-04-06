from collections import Counter
from functools import reduce
import time

temperatures_in_celsius = [20.5, 22.4, 19.8, 21.3, 18.9] 
pollutants = ["CO2", "Ozone", "CO2", "SO2", "CO2"] 
air_quality_index = [45, 62, 150, 55, 112]
#NOTE: Values > 100 are considered "poor" air quality.

humidity_levels = [45, 55, 60, 48, 53]



#1)

#temp conversion
def temp_conversion(*args):
    print(args)
    for cel in args:
        print(cel)
        return(cel * 9/5) + 32
temp_conversion(temperatures_in_celsius,humidity_levels)

print("--------------------------------------------------------------")
#2)
#def convert(arr):
 #   return[(cel * 9/5) + 32 for cel in arr]
#print(convert(temperatures_in_celsius))

print("--------------------------------------------------------------")

#3)
temp_fahrenheit = [*map(lambda cel:(cel*9/5) + 32, temperatures_in_celsius)]
print(temp_fahrenheit)

print("--------------------------------------------------------------")

# Задача 1: Перевести температуры из Цельсия в Фаренгейтыtemperatures_in_fahrenheit = list(map(lambda c: (c * 9/5) + 32, temperatures_in_celsius))

# Задача 2: Идентифицировать значения в индексе качества воздуха, превышающие 100
poor_air_quality = list(filter(lambda aqi: aqi > 100, air_quality_index))

# Задача 3: Определить самый распространенный загрязнитель
most_common_pollutant = Counter(pollutants).most_common(1)[0][0]

# Задача 4: Рассчитать сумму уровней влажности и среднюю влажность
humidity_sum = reduce(lambda x, y: x + y, humidity_levels)
average_humidity = humidity_sum / len(pollutants)

# Задача 5: Сгруппировать данные и вывести информацию
zipped_data = zip(pollutants, temp_fahrenheit, poor_air_quality, pollutants)

for index, (location, temperature, air_quality, pollutant) in enumerate(zipped_data):
    print(f"Location {index + 1}: {location} - Temperature: {temperature}°F, Air Quality: {air_quality}, Most Common Pollutant: {pollutant}")

# Additional information
print(f"The most common pollutant is: {most_common_pollutant}")
print(f"The average humidity is: {average_humidity}")


# Дополнительная информация
print(f"Самый распространенный загрязнитель: {most_common_pollutant}")
print(f"Средняя влажность: {average_humidity}")





def calculate_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time:.4f} seconds to execute.")
        return result
    return wrapper