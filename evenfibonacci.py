total = 0 #assigned variable for sum of even numbers in sequence

i, j = 1, 0 #start of sequence, i and j assigned

while j <= 4000000: #condition for j variable to be less than 4000000
        if j % 2 == 0: 
                total += j 
        i, j = j, i + j

print total