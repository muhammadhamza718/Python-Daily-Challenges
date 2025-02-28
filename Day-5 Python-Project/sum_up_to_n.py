def sum_up_to_n():
    try:
        number = int(input("Enter a number: "))
        total_sum = sum(range(1, number + 1))
        print(f"📌 Output: Sum: {total_sum}")
    except ValueError:
        print("❌ Please enter a valid number.")

sum_up_to_n()
