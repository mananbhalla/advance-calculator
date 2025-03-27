def divide_calculator():
    print("Enter the numbers you want to divide. Type 'confirm' to get the result.")
    numbers = []
    while True:
        inputd = input("Enter a number (or 'confirm' to finish): ")
        if inputd.lower() == "confirm":
            break
        try:
            num = float(inputd)
            # If it's the first number, add it directly (starting point for division)
            if not numbers:
                numbers.append(num)
            else:
                # Calculate the current division result
                current_result = numbers[0]
                for n in numbers[1:]:
                    current_result /= n
                
                # Check if dividing by the new number exceeds the limit
                if num == 0:
                    print("Division by zero is not allowed. Please enter a valid number.")
                elif current_result / num < 1:
                    print("Dividing by this number will result in a value less than 1. Please enter a larger number.")
                else:
                    numbers.append(num)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    # Calculate the total division result
    if numbers:
        total_result = numbers[0]
        for n in numbers[1:]:
            total_result /= n
        print(f"The total result of the division is: {total_result}")
    else:
        print("No numbers were entered.")

divide_calculator()