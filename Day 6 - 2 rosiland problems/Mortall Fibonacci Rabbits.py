n = 89  # Total months
m = 18  # Lifespan in months



def mortal_fibonacci(n, m):
    ages = [1] + [0] * (m - 1)

    for month in range(1, n):
        new_borns = sum(ages[1:])  # rabbits of age ≥1 can reproduce
        # Age rabbits: shift right, oldest dies
        ages = [new_borns] + ages[:-1]

    return sum(ages)
print(mortal_fibonacci(n, m))