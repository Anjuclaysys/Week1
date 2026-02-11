def odd_even_checker():
    """
    check if a given number is odd or even.
    Taking the user input and prints whether it is even or not
    """
    num = int(input("Enter a number: "))
    if num%2 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")


odd_even_checker()