# the two function are defined to handle temperature conversions. 
#These function take a temperature value as input and reture the converted temperature value 
def celsius_to_fahrenheit(celsius):
    return round((celsius * 9/5) + 32, 1)

def fahrenheit_to_celsius(fahrenheit):
    return round((fahrenheit - 32) * 5/9, 1)
# the function is the main part of the code that handles the user interface and the conversion process.
# it runs in a loop until the user chooses to exit.
def convert_temperature():
    #the loop allows the user to make multiple conversion until they decided to exit.
    #the loop continues until the user types exit
    while True:
        unit = input("Is this temperature in Celsius or Fahrenheit (C/F), or type 'exit' to quit: ")

        if unit.lower() == "exit":
            print("Exiting the program.")
            break
        #the user enters an invalid unit, it prints an error message and conditions to the next iteration of the loop.
        # this ensures that the program doesn't crash due to unexpected inputs.
        if unit.upper() not in ["C", "F"]:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
            continue

        try:
            temp = float(input("Enter the temperature: "))

            if unit.upper() == "C":
                converted_temp = celsius_to_fahrenheit(temp)
                print(f"The temperature in Fahrenheit is: {converted_temp}\N{DEGREE SIGN}F")
            elif unit.upper() == "F":
                converted_temp = fahrenheit_to_celsius(temp)
                print(f"The temperature in Celsius is: {converted_temp}\N{DEGREE SIGN}C")
        # if the user enters a non-numeric value, it catches the valueError expection and prints an error message.
        #it promotes the user to enter a valid number 
        except ValueError:
            print("Invalid input. Please enter a valid number.")
# this line of code checks if it's being run as the main script and calls the function to start the temperature conversion program.
if __name__ == "__main__":
    convert_temperature()
