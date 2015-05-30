print sum([i for i in range(1000) if i % 3 == 0 or i % 5 == 0])


#also try this code below where you can define your own max and numbers

def sum_of_divisors(below, divisors):
    return sum((n for n in xrange(below) if 0 in (n % d for d in divisors)))

max = 3560
nums = [5, 17]

print sum_of_divisors(max, nums)