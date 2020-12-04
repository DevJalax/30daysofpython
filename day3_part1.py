def Merge(d1, d2):
	return(d2.update(d1))
	
d1 = {"Maharastra": "Mumbai", "Tamilnadu": "Chennai"}
d2 = {"WB": "Kolkata", "Delhi": "Delhi"}

# This return None
print(Merge(d1, d2))

# changes made in d2
print(d2)