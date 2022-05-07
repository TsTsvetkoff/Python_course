"""
Create a Python function which has to do a temperature conversions as follows:

1. Celsius -> Farenheit
2. Farenheit -> Celsius
3. Farenheit -> Kelvin
4. Kelvin -> Farenheit
5. Kelvin -> Celsius
6. Celsius -> Farenheit // Kelvin ?

The function has to provide a choice from source to target temperature.
"""

temp_conversion = {
    'celsius_farenheit': lambda value : round(value * 9/5 + 32, 2),
    'farenheit_celsius': lambda value: round((value - 32) * 5/9, 2),
    'farenheit_kelvin': lambda value: round((value + 459.67) * 5/9, 2),
    'kelvin_farenheit': lambda value: round(1.8*(value-273.15) + 32, 2),
    'kelvin_celsius': lambda value: round(value-273.15, 2),
    'celsius_kelvin': lambda value: round(value + 273.15, 2),

}
print(temp_conversion['celsius_farenheit'](100))
print(temp_conversion['farenheit_celsius'](100))
print(temp_conversion['farenheit_kelvin'](100))
print(temp_conversion['kelvin_farenheit'](100))
print(temp_conversion['kelvin_celsius'](100))
print(temp_conversion['celsius_kelvin'](100))
