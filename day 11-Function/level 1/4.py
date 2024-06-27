# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.

def celsiusToFahrenheit(celsius):
    result=(celsius * 9/5)+32
    return result

print(celsiusToFahrenheit(100))
print(celsiusToFahrenheit(38))
print(celsiusToFahrenheit(27))