from sys import argv 

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

print "Press y to close the file or N to keep open"
x = raw_input("")
if x == "y":
	txt.close()

elif x == "n":
	txt.read()

print "Lets open a second file:"
file_again = raw_input ("> ")

txt_again = open(file_again)

print txt_again.read()


