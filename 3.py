# Celsius to Kelvin & Fahrenheit

c = float(input("Enter temperature in celsius:"))

kelvin = c + 273.15
fahrenheit = (c * 9/5) + 32

print(f"{c}°C  equals",kelvin,"kelvin and is a", type(kelvin))
print(f"{c}°C equals to",fahrenheit, "fahrenheit and is a", type(fahrenheit))