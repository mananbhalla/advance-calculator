def sum_calculator():
    print("Enter numbers to add (type 'confirm' to calculate the sum):")
    numbers = []
    while True:
        user_input = input("Enter a number (or 'confirm' to finish): ")
        if user_input.lower() == 'confirm':
            break
        try:
            num = int(user_input)
            if sum(numbers) + num > 110:
                print("Adding this number will exceed the limit of 110. Please enter a smaller number.")
            else:
                numbers.append(num)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    total_sum = sum(numbers)
    print(f"The total sum of the entered numbers is: {total_sum}")

sum_calculator()
