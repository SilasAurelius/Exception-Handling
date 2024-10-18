# Task 1: Start Begin by asking the user to enter the temperature in Fahrenheit.

# Task 2: Temperature Conversion Write a function that converts the Fahrenheit temperature to Celsius. Remember that the formula is (Fahrenheit - 32) * 5/9. Use a try block to catch any potential errors during the conversion process. What happens if they type out "thirty" instead of doing 30?

#Task 3: User Experience Implement an else block that prints the converted temperature in a user-friendly format. Example: "100 degrees Fahrenheit is 37.78 degrees Celsius."

# Task 4: Finally Add a finally block that thanks the user for using the weather forecast application, ensuring that this message is displayed regardless of whether an exception was caught or not.
def celsius_conversion(temp_input):
    celsius = (temp_input - 32) * 5/9
    return celsius

while True:
    try:
        temp_input = float(input("Enter the temperature in Fahrenheit: "))
    except ValueError:
        print("Must be numeric.")
    except NameError:
        print("Must be numeric.")
    except Exception as e:
        print("An unexpted error has occured.")
    try:
        if temp_input == -1000000000000000000000:
                    print(f"{temp_input} degrees Fahrenheit is {celsius_conversion(temp_input):.2f} degrees Celsius")
        else:
            print(f"{temp_input} degrees Fahrenheit is {celsius_conversion(temp_input):.2f} degrees Celsius")    
                    # Task 3 required me to use an else block to display the conversion. This confused me because it felt a bit unneccessary.                
    finally:
        print("Thank you for using the Weather Forecast Application!")  
    
celsius_conversion(temp_input)
    

