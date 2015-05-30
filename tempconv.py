#convert celsius to fahrenheit 
print 'Type f to convert from Fahrenheit to Celsius'
print 'Type c to convert from celsius to Fahrenheit'

x = raw_input("")
if x == "f":
	y = raw_input("enter degrees Fahrenheit: ")
	f = (int(y) -32) * 5.0 / 9
	print "%s degrees Fahrenheit is %s degrees Celsius." %(y,f)
	
elif x == "c":
	n = raw_input("enter degrees Celsius: ")
	z = (int(n) * 9) / 5.0 + 32
	print "%s degrees Celsius is %s degrees Fahrenheit." %(n,z)


