months = 36
litter_size = 2

prev = 1  # F(n-2)
curr = 1  # F(n-1)

for _ in range(3, months + 1):
    next_rabbits = curr + litter_size * prev
    prev, curr = curr, next_rabbits

print(months, curr)
#curr = number of pairs last month (F(n−1)).
#prev = number of pairs two months ago (F(n−2)).