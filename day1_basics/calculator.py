def calculator():
    """
    calculator with basic arithemetic operations.
    can perform Addition, substraction,multiplication,division
    """
    print("1. Addition")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter your Choice 1-4: ")

    if choice == "1":
        numbers = []
        while True:
            num = input("Enter numbers(or done to finish): ")
            if num.lower() == "done":
                break
            try:
                numbers.append(float(num))
            except ValueError:
                print("Please enter a valid number")
        if numbers:
            result = sum(numbers)
            print(f"Sum: {result}")
        else:
            print("No numbers to add")

    elif choice == "2":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 - num2
        print(result)
        print(f"Difference : {result}")

    elif choice == "3":
        numbers = []
        while True:
            num = input("Enter a number (done to finish)")
            if num.lower() == "done":
                break
            try:
                numbers.append(float(num))
            except ValueError:
                print("Enter a valid number")
        if numbers:
            result = 1
            for num in numbers:
                result *= num
            print(f"product: {result}")
        else:
            print("No numbers to multiply")
    elif choice == "4":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the Second number should not be 0:"))
        if num2 != 0:
            result = num1 / num2
            print(f"Result:{result}")
        else:
            print("Zero division error")
    else:
        print("invalid choice")

    return result


calculator()
