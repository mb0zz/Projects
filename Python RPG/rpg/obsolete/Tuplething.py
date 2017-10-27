def tuple_casing(string):
	a,b,c,d = string.upper(),string.lower(),string[0].upper(),string[::-1]
	return(a,b,c,d)
x = (tuple_casing("hello, my name is"))
print(x)