# Even and Odd Counter Program
# Even, Odd, and Prime Counter Program
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_count = 0
odd_count = 0
prime_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

    # Prime check
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            prime_count += 1

print("Even numbers:", even_count)
print("Odd numbers:", odd_count)
print("Prime numbers:", prime_count)


