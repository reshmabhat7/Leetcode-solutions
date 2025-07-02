def Solution(n):
    total_sum = 0
    prod = 1

    for i in str(n):
        prod *= int(i)
        total_sum += int(i)

    total = prod - total_sum
    return total
