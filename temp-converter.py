# Program: Temperature Converter 
# Features: Convert Celcius to Fahrenheit and Vice versa
# Procedure:
# 1. Ask for input for temperature
# 2. Select conversion type: Celcius to Farenheit, Vice versa
# 3. Calculate conversion
# 4. Print result

def celcius_to_fahrenheit(celcius):
    """Convert Celsius to Fahrenheit.

    Args:
        celcius (float): The temperature in Celsius.

    Returns:
        float: The temperature converted to Fahrenheit.
    """
    fahrenheit = (celcius * 9/5) + 32
    return fahrenheit


def fahrenheit_to_celcius(fahrenheit):
    """Convert Fahrenheit to Celsius.

    Args:
        fahrenheit (float): The temperature in Fahrenheit.

    Returns:
        float: The temperature converted to Celsius.
    """
    celcius = (fahrenheit - 32) * 5/9
    return celcius

# Start of the program
print("Welcome to Temperature Converter")
temperature = float(input("Enter Temperature: "))
print("Select Conversion Type: \n1. Celsius to Fahrenheit \n2. Fahrenheit to Celsius\n")
conversion_type = int(input("Enter Conversion Type: "))

# Control flow for conversion type
if conversion_type == 1:
    result = celcius_to_fahrenheit(temperature)
    print(f"\n{temperature} Celsius (°C) is equal to {result:.2f} Fahrenheit (°F)")
elif conversion_type == 2:
    result = fahrenheit_to_celcius(temperature)
    print(f"\n{temperature} Fahrenheit (°F) is equal to {result:.2f} Celsius (°C)")
else:
    print("Invalid Conversion Type")




