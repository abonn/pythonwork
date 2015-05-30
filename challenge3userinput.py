def no_dups(seq): #function
    seen = {} #set
    pos = 0 #start at first number
    for number in seq: 
        if number not in seen: 
            seen[number] = True
            seq[pos] = number #number is equal to the next position in the sequence 
            pos += 1 #moves to next number in sequence
    del seq[pos:] #delete duplicate if already seen by function

print "enter a list of numbers separated by commas and 1 space: "
raw_input = "Enter a list of numbers separated by commas and 1 space: "
numbers = raw_input 

no_dups(numbers) #calls function on 1st (the number list to be anaylzed)
print(numbers)