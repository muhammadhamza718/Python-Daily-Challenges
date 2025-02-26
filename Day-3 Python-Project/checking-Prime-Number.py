def is_Prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

prime_Number = int(input("Enter a number: "))

if is_Prime(prime_Number):
    print("Yes, it's a prime number!")
else:
    print("No, it's not a prime number!")