def multiply():
    print("Enter the numbers you want to multiply. Type 'confirm' to get the result.")
    numbers = []
    while True:
        inputd = input("Enter a number (or 'confirm' to finish): ")
        if inputd.lower() == "confirm":
            break
        try:
            num = int(inputd)
            # Calculate the current product of numbers
            current_product = 1
            for n in numbers:
                current_product *= n
            
            # Check if multiplying the new number exceeds the limit
            if current_product * num > 120:
                print("Multiplying this number will exceed the limit of 120. Please enter a smaller number.")
            else:
                numbers.append(num)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    # Calculate the total product of all numbers
    total_product = 1
    for n in numbers:
        total_product *= n
    
    print(f"The total product of the entered numbers is: {total_product}")

multiply()

