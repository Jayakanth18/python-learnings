# Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.

def evens_and_odds(number):
    if number <= 0:
        raise ValueError("The number must be a positive integer.")

    evens = 0
    odds = 0

    while number > 0:
        digit = number % 10
        if digit % 2 == 0:
            evens += 1
        else:
            odds += 1
        number = number // 10

    return evens, odds

# Example usage:
number = 344568
even_count, odd_count = evens_and_odds(number)
print(f"Evens: {even_count}, Odds: {odd_count}")
