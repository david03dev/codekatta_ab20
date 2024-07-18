def calculate_simple_interest(principal, rate, time):
    # Calculate simple interest
    simple_interest = (principal * rate * time) / 100.0
    # Round off to two decimal places
    simple_interest_rounded = round(simple_interest, 2)
    return simple_interest_rounded

# Taking input from user
input_values = input().strip().split()
principal = float(input_values[0])
rate = float(input_values[1])
time = float(input_values[2])

# Calculate and print the simple interest
simple_interest = calculate_simple_interest(principal, rate, time)
print(f"{simple_interest:.2f}")
