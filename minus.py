def subtract_calculator():
    print("Enter numbers to subtract (type 'confirm' to calculate the result):")
    numbers = []
    while True:
        user_input = input("Enter a number (or 'confirm' to finish): ")
        if user_input.lower() == 'confirm':
            break
        try:
            num = int(user_input)
            # If it's the first number, add it directly (starting point for subtraction)
            if not numbers:
                numbers.append(num)
            else:
                # Calculate the current subtraction result
                current_result = numbers[0] - sum(numbers[1:])
                if current_result - num < -110:
                    print("Subtracting this number will exceed the limit of -110. Please enter a smaller number.")
                else:
                    numbers.append(num)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    # Calculate the total subtraction result
    if numbers:
        total_result = numbers[0] - sum(numbers[1:])
        print(f"The total result of the subtraction is: {total_result}")
    else:
        print("No numbers were entered.")

subtract_calculator()
