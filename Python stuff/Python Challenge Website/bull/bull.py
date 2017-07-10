import time

a = "1"

def get_num(integer, numtofind):
	count = 0
	for index in integer:
		if index == numtofind:
			count += 1
		else:
			break
	return(count)
	
def slicer(oc_list,a):
	
	
	while len(a) >= 1:
	
		i = a[:1]
		occurs = get_num(a, i)
		oc_list.append((occurs, i))

		a = a[occurs:]
		
		#slicer(oc_list,a)

	return(oc_list)

cycle = 0
	
while cycle < 30:
	oc_list = []
	cycle = cycle + 1
	#time.sleep(3)
	oc_list = slicer(oc_list,a)
	
	a = ""
	for tuple in oc_list:
		int,string = tuple
		a = a + str(int) + string
	print(a)
print(len(a))
	

	


