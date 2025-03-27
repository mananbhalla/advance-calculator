from minus import subtract_calculator
from sum import sum_calculator
from multiply import multiply
from devide import divide_calculator
print("27th march , thrusday , 11:30 am ")
print("made with the help of ai 4.0 github capitior")
def main():
    print("Welcome to the Advanced Calculator!")
    print("Select an operation:")
    print("1. Sum")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    while True:
        choice = input("Enter the number corresponding to your choice (1-4) or 'exit' to quit: ").strip()
        
        if choice == '1':
            print("\nYou selected: Sum")
            sum_calculator()
        elif choice == '2':
            print("\nYou selected: Subtract")
            subtract_calculator()
        elif choice == '3':
            print("\nYou selected: Multiply")
            multiply()
        elif choice == '4':
            print("\nYou selected: Divide")
            divide_calculator()
        elif choice.lower() == 'exit':
            print("Exiting the calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option (1-4) or type 'exit' to quit.")

if __name__ == "__main__":
    main()
